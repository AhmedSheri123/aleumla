from django.shortcuts import render
from services.models import Saudi, Turkish, show_in_index, Dollars, Euros, Golds
from .functions import  dollars_id, Euros_id, Golds_id, Turkish_id, Saudi_id
# Create your views here.

def index(request):
    shows = show_in_index.objects.filter(is_show=True)
    dols = Dollars.objects.all()
    eurs = Euros.objects.all()
    gols = Golds.objects.all()
    turkish = Turkish.objects.all()
    saudi = Saudi.objects.all()
    
    
    item = {
        'dol_ids' : dollars_id(show_in_index, Dollars),
        'eur_ids': Euros_id(show_in_index, Euros),
        'gol_ids': Golds_id(show_in_index, Golds),
        'tur_ids': Turkish_id(show_in_index, Turkish),
        'sau_ids': Saudi_id(show_in_index, Saudi),
        'dollars' : dols,
        'euros' : eurs,
        'golds' : gols,
        'shows' : shows,
        'turkish' : turkish,
        'saudi' : saudi,
    }


    return render(request, 'pages/index.html', item)

