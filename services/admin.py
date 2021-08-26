from django.contrib import admin
from .models import Type, City, Materials, Dollars, Euros, Golds, show_in_index, Details, Turkish, Saudi

# Register your models here.

admin.site.register(Type)
admin.site.register(City)
admin.site.register(Materials)
admin.site.register(Dollars)
admin.site.register(Euros)
admin.site.register(Golds)
admin.site.register(show_in_index)
admin.site.register(Details)
admin.site.register(Turkish)
admin.site.register(Saudi)