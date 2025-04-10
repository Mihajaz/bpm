from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Worker(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='worker')
    poste = models.CharField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return self.user_id.username if self.user_id else "Employé sans utilisateur"
    
    
#Technicien
class Technician(models.Model):
    first_name = models.CharField(
        max_length=50,
        help_text='nom du technicien'
    )
    
    last_name = models.CharField(
        max_length=50,
        help_text='prenom du technicien'
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#mission 
class Mission(models.Model):
    # Champs existants
    techniciens = models.ManyToManyField(Technician, related_name="missions")
    bluedesk_link = models.CharField(
        max_length=300,
        help_text='lien bluedesk',
        verbose_name='Bluedesk Link',
        default='https://bluedesk.example.com'
    )
    mission_details = models.TextField(
        help_text='details de la mission',
        verbose_name='Mission Details'
    )
    start_date = models.DateField(
        help_text='date de debut de la mission',
        verbose_name='Start Date'
    )
    start_hour = models.TimeField(
        help_text='heure de debut de la mission',
        verbose_name='Start Hour'
    )
    end_date = models.DateField(
        help_text='date de fin de la mission',
        verbose_name='End Date'
    )
    end_hour = models.TimeField(
        help_text='heure de fin de la mission',
        verbose_name='End Hour'
    )
    location = models.CharField(
        max_length=50,
        help_text='lieu de la mission'
    )
    facturation = models.BooleanField(
        help_text='facturation de la mission, facturee ou non',
        verbose_name='Facturation'
    )
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('REFUSED', 'Refused'),
        ('VALIDATED', 'Validated'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='NEW',
        verbose_name='Status',
        help_text='Statut de la mission'
    )
    refusal_reason = models.TextField(
        blank=True,
        null=True,
        verbose_name='Refusal Reason',
        help_text='Motif de refus de la mission'
    )
    
    # Nouveaux champs pour le suivi des dates
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
        help_text='Date et heure de création de la mission'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
        help_text='Date et heure de la dernière modification de la mission'
    )
    validated_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Date de validation',
        help_text='Date et heure de validation de la mission'
    )
    refused_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Date de refus',
        help_text='Date et heure de refus de la mission'
    )
    
    # Méthode pour mettre à jour automatiquement les dates de validation/refus
    def save(self, *args, **kwargs):
        # Si c'est un nouvel objet (pas encore en base)
        if not self.id:
            super().save(*args, **kwargs)
            return
            
        # Récupérer l'ancien état pour comparaison
        try:
            old_mission = Mission.objects.get(id=self.id)
            old_status = old_mission.status
        except Mission.DoesNotExist:
            old_status = None
        
        # Si le statut a changé vers VALIDATED, enregistrer la date
        if self.status == 'VALIDATED' and old_status != 'VALIDATED':
            self.validated_at = datetime.datetime.now()
        
        # Si le statut a changé vers REFUSED, enregistrer la date
        if self.status == 'REFUSED' and old_status != 'REFUSED':
            self.refused_at = datetime.datetime.now()
            
        super().save(*args, **kwargs)
        
    class Meta:
        permissions = [
            ("can_validate_mission","Peut valider une mission"),
            ("can_refuse_mission","Peut refuser une mission"),
            ]
    

   
    #depenses 
class Expense(models.Model):
    
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="depenses")
    
    hosting_days = models.IntegerField(
        help_text='nombre de jours de sejour',
        default=0.0,
    )
    
    overnight_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text='tarif nuitée'
    )
    
    total_hosting = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=' pris total de séjour',
        editable = False 
    )

    
    meal_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix des repas',
    )
    
    total_meal_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix total des repas',
        editable = False,
        default=0.00,
    )
    
    
    transport = models.CharField(
        max_length=100,
        help_text='transport',
    )
    
    shipping_costs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='frais de transport',
    )
    
    various_expenses_details = models.CharField(
        max_length=100,
        help_text='divers frais',
    )
    
    various_expenses_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix des divers frais',
    )
    
    total_expenses = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='prix total des frais',
        editable = False,
        default=0.00,
    )
    
    def save(self, *args, **kwargs):
        # Calcul automatique du total_hosting = hosting_days * overnight_rate
        self.total_hosting = self.hosting_days * self.overnight_rate
        
        #calcul du total_meal_costs = hosting_days * meal_costs
        self.total_meal_costs = self.hosting_days * self.meal_costs
         
        #calcul des total_expenses = total_hosting + total_meal_costs + shipping_costs + various_expenses_price
        self.total_expenses = self.total_hosting + self.total_meal_costs + self.shipping_costs + self.various_expenses_price
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.total_expenses}"
        
   
    
    


    
    
    
    
    
    

    
    


    
    


    
    
    
    
    
    

    
    


    