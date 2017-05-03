from django.db import models
import uuid
# Create your models here.
class Entry(models.Model):
    catNumber = models.CharField(max_length=15, blank=True, null=True)
    siteNumber = models.CharField(max_length=120, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    site = models.CharField(max_length=120, blank=True, null=True)
    fileName = models.CharField(max_length=120, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    situation = models.TextField(blank=True, null=True)
    uid=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    def shortInfo(self):
        return {"catNumber": self.catNumber, "situation": self.situation, "uuid": self.uid}
    def toDict(self):
    	return {"catNumber": self.catNumber, \
    			"siteNumber": self.siteNumber, \
    			"locality": self.locality, \
    			"site": self.site, \
    			"name": self.name, \
    			"situation": self.situation, \
                "uuid": self.uid}