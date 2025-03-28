from django.urls import path
from .views import MissionListView, HistoryView, RegisterView , CustomLoginView ,CustomLogoutView,EditMissionView
from . import views
urlpatterns = [
    path('', MissionListView.as_view(), name='missions'),
    path('history/',HistoryView.as_view(),name='history'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit_mission/<int:mission_id>/', EditMissionView.as_view(), name='edit_mission'),
    path('mission/validate/', views.ValidateMissionView.as_view(), name='validate_mission'),
    path('mission/refuse/', views.RefuseMissionView.as_view(), name='refuse_mission'),
    
      
]
