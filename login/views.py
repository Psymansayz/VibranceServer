from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

# Create your views here.
@csrf_exempt
def login(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'username' in data and 'password' in data:
			if User.objects.filter(username=data.get("username")):
				user_instance = User.objects.get(username= data.get("username"))
				if user_instance.password == data.get("password"):
					retData = {
						'id': user_instance.id
					}
					return JsonResponse(retData)
			return HttpResponseBadRequest('invalid username and password')
		return HttpResponseBadRequest('Post did not include username and password')
	else:
		return HttpResponseBadRequest('Post login only')

@csrf_exempt
def create(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'username' in data and 'password' in data:
			if User.objects.filter(username = data.get("username")):
				return HttpResponseBadRequest('username already used')
			else:
				instance = User.objects.create(username = data.get("username"), password = data.get("password"))
				retData = {
					'id': instance.id
				}
				return JsonResponse(retData)
		return HttpResponseBadRequest('Post did not include username and password')
	else:
		return HttpResponseBadRequest('Post new user only')