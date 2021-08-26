from django.shortcuts import render
from .models import Type, City, Materials, Dollars, Euros, Golds, Turkish, Saudi, Details
# Create your views here.



def type(request):
    type = Type.objects.all()
    item = {
        'type' : type
    }
    return render(request, 'services/type.html', item)




def city(request, id):
    city = City.objects.all()

    item = {
        "city": city,
        'type_id' : id,
    }
    return render(request, 'services/city.html', item)




def materials(request, type_id, city_id):

    materials = Materials.objects.all()
    
    item = {
        'material': materials,
        'type_id' : type_id,
        'city_id' : city_id,
    }
    return render(request, 'services/materials.html', item)




def card(request,type_id, city_id, materials_id):

    result2 = None
    card = None
    try:
        if materials_id == 1:
            card = Dollars.objects.filter(type=type_id, city=city_id)            
            result2 = card[1]
        elif materials_id == 2:
            card = Euros.objects.filter(type=type_id, city=city_id)
            result2 = card[1]
        elif materials_id ==3:
            card = Golds.objects.filter(type=type_id, city=city_id)
            result2 = card[1]
        elif materials_id ==4:
            card = Turkish.objects.filter(type=type_id, city=city_id)
            result2 = card[1]
        elif materials_id ==5:
            card = Saudi.objects.filter(type=type_id, city=city_id)
            result2 = card[1]
    except:
        pass
    item = {
        'cards': card,
        'result2': result2,
    }
    return render(request, 'services/card.html', item)

def details(request):
    
    details = Details.objects.filter(is_enable=True)
    dollars = Dollars.objects.all()
    euros = Euros.objects.all()
    golds = Golds.objects.all()
    turkish = Turkish.objects.all()
    saudi = Saudi.objects.all()
    
    buy_list = []

    buy_list.append(dollars[0].sell)
    buy_list.append(euros[0].sell)
    buy_list.append(turkish[0].sell)
    buy_list.append(saudi[0].sell)

    
    item = {
        'saus' : saudi,
        'turs' : turkish, 
        'eurs' : euros,
        'gols' : golds,
        'dols' : dollars,
        'dets' : details,
        'buy_list': buy_list,
    }
    return render(request, 'services/details.html', item)