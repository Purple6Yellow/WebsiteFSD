from django.contrib import admin
#nieuw toegevoegd om model (Post) toe te voegen aan adminstratieomgeving 
from .models import Post

admin.site.register(Post)
