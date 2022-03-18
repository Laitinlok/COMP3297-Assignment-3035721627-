from django.shortcuts import render
import requests
from hyperlink import URL
import json

dataquery= {
	"resource": "http://www.chp.gov.hk/files/misc/occupancy_of_quarantine_centres_eng.csv",
	"section":1,
	"format":"json",
}
centresquery={
	"resource": "http://www.chp.gov.hk/files/misc/no_of_confines_by_types_in_quarantine_centres_eng.csv",
	"section":1,
	"format":"json",
}


dataresponse= requests.get("https://api.data.gov.hk/v2/filter", params=dataquery)
datadict=json.loads(dataresponse)
centresresponse= requests.get("https://api.data.gov.hk/v2/filter", params=centresquery)
centresdict=json.loads(centresresponse)

def dashboard1(request):
	context = {
		"data": 'datadict',
		"centre": 'centresdict',
		},
	return render(request, 'dashboard1.html', context=context)

def dashboard2(request):
	context = {
		"data": 'datadict',
		"centre": 'centresdict',
		},
	return render(request, 'dashboard2.html', context=context)

def dashboard3(request):
	context = {
		"data": 'datadict',
		"centre": 'centresdict',
		},
	return render(request, 'dashboard1.html', context=context)



# Create your views here.
