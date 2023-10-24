from django.shortcuts import render
# later toegevoegd:
from django.utils import timezone
# later toegevoegd (model Post geimporteerd uit het bestand 'models.py'):
from .models import Post

# functie die de berichten op publicatiedatum rangschikt. Hiervoor is een tijdzonepakket geimporteerd. 
# de query die dit doet, is posts genoemd. Deze wordt meegenomen in het html bestand.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})

# retourneert de waarde van een andere functie: de ingebouwde render-functie die een URL-verzoek als parameter neemt en vervolgens de
# template met  .html-extensie opent en opvult met de inhoud. 


# uitbreiding views.py bestand, om te zorgen dat de objecten zal 'uitpakken'(lees: de objecten opvragen die zijn opgeslagen als het model Post)
