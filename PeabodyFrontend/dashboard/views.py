from .models import Entry
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from itertools import chain
# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html')

def getSearchResults(request, limit=10):
	# try:
	query = request.POST.get("queryBar")
	catNumberResults = queryToDict(Entry.objects.filter(catNumber__contains=query))
	siteNumberResults = queryToDict(Entry.objects.filter(siteNumber__contains=query))
	localityResults = queryToDict(Entry.objects.filter(locality__contains=query))
	siteResults = queryToDict(Entry.objects.filter(site__contains=query))
	nameResults = queryToDict(Entry.objects.filter(name__contains=query))
	situationResults = queryToDict(Entry.objects.filter(situation__contains=query))
	results = catNumberResults+siteNumberResults+localityResults+siteResults+nameResults+situationResults
	return JsonResponse(results[:limit], safe=False)
	# except:
		# return HttpResponseRedirect("/dashboard")

def queryToDict(queryResults):
	daList = []
	for res in queryResults:
		daList.append(Entry.toDict(res))
	return daList