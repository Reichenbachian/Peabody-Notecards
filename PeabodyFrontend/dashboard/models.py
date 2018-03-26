from django.db import models
import uuid
import base64
import os.path
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
# Create your models here.
class Entry(models.Model):
    catNumber = models.IntegerField(null=True,blank=True,default=0)
    accNum=models.IntegerField(null=True,blank=True,default=0)
    name = models.TextField(blank=True, null=True)
    site = models.CharField(max_length=120, blank=True, null=True)
    siteNumber = models.CharField(max_length=120, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    situation = models.TextField(blank=True, null=True)
    fileName = models.CharField(max_length=120, blank=True, null=True)
    uid=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['accNum', 'catNumber']

    def shortInfo(self):
        return {"Catalog Number": self.catNumber,
                "Accession Number": self.accNum,
                "Name": self.name,
                "Site": self.site,
                "Site Number": self.siteNumber,
                "Locality": self.locality,
                "Situation": self.situation,
                "Image": self.fileName,
                "uuid": self.uid,
                "Created At": self.created_at,
                "Updated At": self.updated_at,}
    def fullInfo(self):
        fileLocation = SITE_ROOT+"/../../"+self.fileName
        print("HERE:", fileLocation)
        with open(fileLocation, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return {"Catalog Number": self.catNumber,
                "Accession Number": self.accNum,
                "Name": self.name,
                "Site": self.site,
                "Site Number": self.siteNumber,
                "Locality": self.locality,
                "Situation": self.situation,
                "Image": encoded_string,
                "uuid": self.uid,
                "Created At": self.created_at,
                "Updated At": self.updated_at,}
