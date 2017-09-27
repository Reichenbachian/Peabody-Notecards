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

def apiCall(request, limit=100):
	# try:
	if "queryBar" in request.POST.keys():
		query = request.POST.get("queryBar")
		catNumberResults = queryToDict(Entry.objects.filter(catNumber__contains=query))
		accNumResults = queryToDict(Entry.objects.filter(accNum__contains=query))
		siteNumberResults = queryToDict(Entry.objects.filter(siteNumber__contains=query))
		localityResults = queryToDict(Entry.objects.filter(locality__contains=query))
		siteResults = queryToDict(Entry.objects.filter(site__contains=query))
		nameResults = queryToDict(Entry.objects.filter(name__contains=query))
		situationResults = queryToDict(Entry.objects.filter(situation__contains=query))
		results = catNumberResults+siteNumberResults+localityResults+siteResults+nameResults+situationResults+accNumResults
		return JsonResponse(results[:limit], safe=False)
	elif "value" in request.POST.keys():
		uuid = request.POST.get("uuid")
		pk = request.POST.get("pk")
		val = request.POST.get("value")
		result = Entry.objects.get(uid=uuid)
		if request.POST.get("name") == "locality":
			print(result.locality)
			result.locality = val;
			print(result.locality)
		elif request.POST.get("name") == "site":
			result.site = val;
		elif request.POST.get("name") == "name":
			result.name = val;
		elif request.POST.get("name") == "situation":
			result.situation = val;
		result.save();
		print(uuid)
		return JsonResponse({"Success": True})
	elif "uuid" in request.POST.keys():
		result = Entry.objects.get(uid=request.POST.get("uuid"))
		result.fullInfo()
		return JsonResponse(result.fullInfo(), safe=False)
	print("redirecting")
	return HttpResponseRedirect("/dashboard")

def queryToDict(queryResults, short=True):
	daList = []
	for res in queryResults:
		if not short:
			daList.append(Entry.fullInfo(res))
		else:
			daList.append(Entry.shortInfo(res))
	return daList

def imgs(request):
	valid_image="imgs/"
	try:
	    with open(valid_image, "rb") as f:
	        return HttpResponse(f.read(), content_type="image/jpeg")
	except IOError:
	    red = Image.new('RGBA', (1, 1), (255,0,0,0))
	    response = HttpResponse(content_type="image/jpeg")
	    red.save(response, "JPEG")
	    return response
