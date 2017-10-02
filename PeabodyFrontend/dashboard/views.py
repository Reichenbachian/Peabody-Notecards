from .models import Entry
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from itertools import chain
from django.utils import timezone
# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html')

def apiCall(request, limit=200):
	# try:
	if "queryBar" in request.POST.keys():
		query = request.POST.get("queryBar")
		catNumberResults = queryToDict(Entry.objects.filter(catNumber__contains=query))
		accNumResults = queryToDict(Entry.objects.filter(accNum__contains=query))
		nameResults = queryToDict(Entry.objects.filter(name__contains=query))
		siteResults = queryToDict(Entry.objects.filter(site__contains=query))
		siteNumberResults = queryToDict(Entry.objects.filter(siteNumber__contains=query))
		localityResults = queryToDict(Entry.objects.filter(locality__contains=query))
		situationResults = queryToDict(Entry.objects.filter(situation__contains=query))
		results = catNumberResults+accNumResults+nameResults+siteResults+siteNumberResults+localityResults+situationResults
		return JsonResponse(results[:limit], safe=False)
	elif "queryBarAcc" in request.POST.keys():
		query = request.POST.get("queryBarAcc")
		accNumResults = queryToDict(Entry.objects.filter(accNum=query))
		results = accNumResults
		return JsonResponse(results[:limit], safe=False)
	elif "value" in request.POST.keys():
		uuid = request.POST.get("uuid")
		pk = request.POST.get("pk")
		val = request.POST.get("value")
		result = Entry.objects.get(uid=uuid)
		if request.POST.get("name") == "name":
			print(result.name)
			result.name = val
			result.updated_at = timezone.now()
			print(result.name)
		elif request.POST.get("name") == "site":
			result.site = val
			result.updated_at = timezone.now()
		elif request.POST.get("name") == "locality":
			result.locality = val
			result.updated_at = timezone.now()
		elif request.POST.get("name") == "situation":
			result.situation = val
			result.updated_at = timezone.now()
		result.save()
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
