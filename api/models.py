from django.db import models
from django.db.models.fields import CharField, DateTimeField
import datetime
class Firmware(models.Model):
    headers = models.JSONField()
    link = CharField(max_length=500)
    filename = CharField(max_length=500)
    firmware_version = CharField(max_length= 1500)
    region = CharField(max_length=100,default="INS")
    model = CharField(max_length=100,default="SM-N975F")
    date = DateTimeField(auto_now=True)
    status = CharField(default="found",max_length=10)
    def __str__(self) :
        return self.filename

class Post(models.Model):
    post_title = CharField(max_length=500)
    content = CharField(max_length=500)
    meta_title = CharField(max_length=100)
    meta_description = CharField(max_length=500)
    medifire_link = CharField(max_length=1000)
    gdrive_link = CharField(max_length=1000)
    megadrive_link = CharField(max_length=1000)
    published_date = DateTimeField(auto_now_add=True)
    firmware_version = models.ForeignKey(Firmware,on_delete=models.CASCADE)

    def __str__(self) :
        return self.post_title