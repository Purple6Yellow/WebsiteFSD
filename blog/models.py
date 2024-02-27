from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    Datum = models.DateField(blank=True, null= True)
    Tijdstip_start = models.TimeField(blank=True, null= True)
    Tijdstip_eind = models.TimeField(blank=True, null= True)
    Kosten = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null = True)
    Omschrijving = models.TextField()
    published_date = models.DateTimeField(blank=True, null= True)

    def publish (self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        + self.Datum
        + str(self.author)
        + self.Tijdstip_start

        
        
        
        # + '__' + str(self.author)



