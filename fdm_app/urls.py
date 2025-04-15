from django.urls import path
from .views import MissionListView, HistoryView, RegisterView , CustomLoginView ,CustomLogoutView,EditMissionView,GeneratePDFView,ExportMissionsPDFView,ExportMissionsExcelView,ExportMissionsCSVView
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
    path('mission/<int:mission_id>/download_pdf/', GeneratePDFView.as_view(), name='download_pdf'),
    path('export/pdf/', ExportMissionsPDFView.as_view(), name='export_pdf'),
    path('export/excel/', views.ExportMissionsExcelView.as_view(), name='export_excel'),
    path('export/csv/', views.ExportMissionsCSVView.as_view(), name='export_csv'),
]
