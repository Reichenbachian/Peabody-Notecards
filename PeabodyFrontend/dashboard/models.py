from django.db import models
import uuid
import base64
import os.path
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
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
    accNum=models.CharField(max_length=10, blank=True)
    def shortInfo(self):
        return {"catNumber": self.catNumber, "situation": self.situation, "uuid": self.uid}
    def fullInfo(self):
        fileLocation = SITE_ROOT+"/imgs/"+self.fileName
        print("HERE:", fileLocation)
        with open(fileLocation, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
    	return {"catNumber": self.catNumber, \
    			"siteNumber": self.siteNumber, \
    			"locality": self.locality, \
    			"site": self.site, \
    			"name": self.name, \
    			"situation": self.situation, \
                "accNum": self.accNum, \
                "image": encoded_string, \
                "uuid": self.uid}