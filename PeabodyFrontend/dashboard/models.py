from django.db import models

# Create your models here.
class Entry(models.Model):
    catNumber = models.CharField(max_length=15, blank=True, null=True)
    siteNumber = models.CharField(max_length=70, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    site = models.CharField(max_length=70, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)
    situation = models.TextField(blank=True, null=True)
    def toDict(self):
    	return {"catNumber": self.catNumber, \
    			"siteNumber": self.siteNumber, \
    			"locality": self.locality, \
    			"site": self.site, \
    			"name": self.name, \
    			"situation": self.situation}