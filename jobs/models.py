from django.db import models

# Create your models here.
class Job(models.Model):
    #ImageField
    image=models.ImageField(upload_to='images/')
    #summary
    summary=models.CharField(max_length=200)

    #for changin the job objects name in django admin to something meaningful
    def __str__ (self):
        return self.summary
