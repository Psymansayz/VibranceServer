from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message, DoctorMessage, Note, Notification
import json
# Create your views here.
@csrf_exempt
def messages(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'sender' in data and 'body' in data and 'id' in data:
			Message.objects.create(userId = data.get('id'), sender=data.get('sender'), body =data.get('body'))
			return HttpResponse("message created")
		return HttpResponseBadRequest('missing fields in post request')
	elif request.method == "GET":
		if request.GET.get('id'):
			if Message.objects.filter(userId=request.GET.get('id')):
				return JsonResponse(list(Message.objects.filter(userId=request.GET.get('id')).values()), safe=False)
			return HttpResponseBadRequest('no messages found')
		return HttpResponseBadRequest('no user id found')
@csrf_exempt
def doctorMessages(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'sender' in data and 'body' in data and 'id' in data:
			DoctorMessage.objects.create(userId = data.get('id'), sender=data.get('sender'), body =data.get('body'))
			return HttpResponse("Doctor message created")
		return HttpResponseBadRequest('missing fields in post request')
	elif request.method == "GET":
		if request.GET.get('id'):
			if DoctorMessage.objects.filter(userId=request.GET.get('id')):
				return JsonResponse(list(DoctorMessage.objects.filter(userId=request.GET.get('id')).values()), safe=False)
			return HttpResponseBadRequest('no Doctor messages found')
		return HttpResponseBadRequest('no user id found')
@csrf_exempt
def notes(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'topic' in data and 'body' in data and 'id' in data:
			Note.objects.create(userId = data.get('id'), topic=data.get('topic'), body =data.get('body'))
			return HttpResponse("Note created")
		return HttpResponseBadRequest('missing fields in post request')
	elif request.method == "GET":
		if request.GET.get('id'):
			if Note.objects.filter(userId=request.GET.get('id')):
				return JsonResponse(list(Note.objects.filter(userId=request.GET.get('id')).values()), safe=False)
			return HttpResponseBadRequest('no Notesfound')
		return HttpResponseBadRequest('no user id found')
@csrf_exempt
def notifications(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'title' in data and 'body' in data and 'id' in data:
			Notification.objects.create(userId = data.get('id'), topic=data.get('title'), body =data.get('body'))
			return HttpResponse("Notification created")
		return HttpResponseBadRequest('missing fields in post request')
	elif request.method == "GET":
		if request.GET.get('id'):
			if Notification.objects.filter(userId=request.GET.get('id')):
				return JsonResponse(list(Notification.objects.filter(userId=request.GET.get('id')).values()), safe=False)
			return HttpResponseBadRequest('no Notifications found')
		return HttpResponseBadRequest('no user id found')
@csrf_exempt
def deleteNotification(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data:
			if Notification.objects.filter(id = data.get('id')):
				Notification.objects.filter(id = data.get('id')).delete()
				return HttpResponse("Notification deleted")
			return HttpResponseBadRequest("notification not found")
		return HttpResponseBadRequest('missing fields in post request')
@csrf_exempt
def deleteNote(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data:
			if Note.objects.filter(id = data.get('id')):
				Note.objects.filter(id = data.get('id')).delete()
				return HttpResponse("Note deleted")
			return HttpResponseBadRequest("note not found")
		return HttpResponseBadRequest('missing fields in post request')
@csrf_exempt
def deleteDoctorMessage(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data:
			if DoctorMessage.objects.filter(id = data.get('id')):
				DoctorMessage.objects.filter(id = data.get('id')).delete()
				return HttpResponse("doctor message deleted")
			return HttpResponseBadRequest("doctor message not found")
		return HttpResponseBadRequest('missing fields in post request')
@csrf_exempt
def deleteMessage(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data:
			if Message.objects.filter(id = data.get('id')):
				Message.objects.filter(id = data.get('id')).delete()
				return HttpResponse("message deleted")
			return HttpResponseBadRequest("message not found")
		return HttpResponseBadRequest('missing fields in post request')


