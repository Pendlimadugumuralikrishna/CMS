from django.db import models

# Create your models here.
class package(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    track_id = models.IntegerField(null=True)
    service = models.CharField(max_length=100,default="dtdc")

    def __str__(self):
       return f"{self.name} your package has been received and delivered to you shortly by {self.service} service providers and trackid is {self.track_id} "
        
