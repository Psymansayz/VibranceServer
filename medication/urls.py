from django.urls import path
from . import views

urlpatterns = [
	path('', views.medicationInfo, name = 'medicationInfo'),
	path('new/', views.newMedication, name= 'newMedication'),
	path('delete/', views.deleteMedication, name= 'deleteMedication'),
]