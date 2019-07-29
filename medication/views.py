from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Medication
from datetime import datetime
import json
# Create your views here.
@csrf_exempt
def medicationInfo(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data and 'color' in data:
			medication_instance = Medication.objects.filter(userId=data.get("id"))
			if medication_instance and medication_instance.filter(color=data.get("color")):
				medication_single = medication_instance.get(color=data.get("color"))
				if medication_single.adherence:
					retData = json.loads(medication_single.adherence)
					retData['times'].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
					medication_single.adherence = json.dumps(retData)
					medication_single.save(update_fields=['adherence'])
				else:
					retData = {
						'times' :[]
					}
					retData['times'].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
					medication_single.adherence = json.dumps(retData)
					medication_single.save(update_fields=['adherence'])
				return HttpResponse(medication_single.adherence)
			return HttpResponseBadRequest("no medication of that color found")
		return HttpResponseBadRequest("no id and color field found in post request")
	if request.method == "GET":
		if request.GET.get('id'):
			medication_instance = Medication.objects.filter(userId=request.GET.get('id'))
			if medication_instance:
				if request.GET.get('color'):
					if medication_instance and medication_instance.filter(color=request.GET.get("color")):
						return JsonResponse(list(medication_instance.filter(color=request.GET.get("color")).values()), safe=False)
					return HttpResponseBadRequest("no medicaiton of that color")
				return JsonResponse(list(medication_instance.values()), safe=False)
			return HttpResponseBadRequest("no medications found for that id")
		return HttpResponseBadRequest("no id found")
@csrf_exempt
def newMedication(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data and 'name' in data and 'color' in data and 'dosage' in data and 'frequency' in data and 'refillDate' in data:
			if Medication.objects.filter(userId=data.get('id')).filter(color=data.get('color')):
				return HttpResponseBadRequest("color already used")
			Medication.objects.create(userId =data.get('id'), name= data.get('name'), color=data.get('color'),dosage=data.get('dosage'),frequency=data.get("frequency"),refillDate=data.get("refillDate"))
			return HttpResponse("medicaiton added")
		return HttpResponseBadRequest("missing or invalid paramaters")
@csrf_exempt
def deleteMedication(request):
	if request.method == "POST":
		data = json.loads(request.body)
		if 'id' in data and 'color' in data:
			if Medication.objects.filter(userId=data.get('id')).filter(color=data.get('color')):
				Medication.objects.filter(userId=data.get('id')).filter(color=data.get('color')).delete()
				return HttpResponse("deleted")
			return HttpResponseBadRequest('no medication of that color found')
		return HttpResponseBadRequest('no id and color in post request')
