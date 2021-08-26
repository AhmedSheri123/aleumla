def dollars_id(show_in_index, Dollars):
    city_list = []
    dol_id_list = []
    shows = show_in_index.objects.filter(is_show=True)
    dols = Dollars.objects.all()
    for show in shows:
        for dol in dols:
            if show.type == dol.type and show.city == dol.city and show.materials == dol.materials:
                if dol.city.id not in city_list:
                    city_list.append(dol.city.id)
                    dol_id_list.append(dol.id)
    return dol_id_list                
    
                     
                         





def Euros_id(show_in_index, Euros):
    city_list = []
    dol_id_list = []
    shows = show_in_index.objects.filter(is_show=True)
    eurs = Euros.objects.all()
    for show in shows:
        for dol in eurs:
            if show.type == dol.type and show.city == dol.city and show.materials == dol.materials:
                if dol.city.id not in city_list:
                    city_list.append(dol.city.id)
                    dol_id_list.append(dol.id)
    return dol_id_list                    





def Turkish_id(show_in_index, Turkish):
    city_list = []
    dol_id_list = []
    shows = show_in_index.objects.filter(is_show=True)
    eurs = Turkish.objects.all()
    
        
    for show in shows:
        for dol in eurs:
            if show.type == dol.type and show.city == dol.city and show.materials == dol.materials:
                if dol.city.id not in city_list:
                    
                    city_list.append(dol.city.id)
                    dol_id_list.append(dol.id)
    return dol_id_list
    



def Saudi_id(show_in_index, Saudi):
    city_list = []
    dol_id_list = []
    shows = show_in_index.objects.filter(is_show=True)
    eurs = Saudi.objects.all()
    for show in shows:
        for dol in eurs:
            if show.type == dol.type and show.city == dol.city and show.materials == dol.materials:
                if dol.city.id not in city_list:
                    city_list.append(dol.city.id)
                    dol_id_list.append(dol.id)
    return dol_id_list




def Golds_id(show_in_index, Golds):
    city_list = []
    dol_id_list = []
    shows = show_in_index.objects.filter(is_show=True)
    gols = Golds.objects.all()
    for show in shows:
        for dol in gols:
            if show.type == dol.type and show.city == dol.city and show.materials == dol.materials:
                if dol.city.id not in city_list:
                    city_list.append(dol.city.id)
                    dol_id_list.append(dol.id)
    return dol_id_list