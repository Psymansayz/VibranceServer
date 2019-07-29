from django.urls import path
from . import views

urlpatterns = [
	path('', views.messages, name = 'messages'),
	path('doctor/', views.doctorMessages, name= 'doctorMessages'),
	path('delete/', views.deleteMessage, name= 'deleteMessage'),
	path('deleteDoctor/', views.deleteDoctorMessage, name ='deleteDoctorMessage'),
	path('notes/', views.notes, name='notes'),
	path('deleteNote/', views.deleteNote, name= 'deleteNote'),
]