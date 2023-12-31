from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey (settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
       return self.title

#class Post(models.Model):
    #Datum = models.DateField(default=timezone.now)
    #Title = models.CharField(max_length=200)
    #Tijdstip_aanvang = models.TimeField(blank=True,null =True)
    #Tijdstip_einde = models.TimeField(blank=True,null =True)
    #Omschrijving = models.TextField()
    #Kosten = models.DecimalField(decimal_places=2,max_digits=10, default='')
    #published_date=models.DateField(default=timezone.now)
    