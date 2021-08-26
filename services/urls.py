from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.details, name='details'),
    path('type', views.type, name='type'),
    path('city/<int:id>', views.city, name='city'),
    path('materials/<int:type_id>/<int:city_id>', views.materials, name='materials'),
    path('card/<int:type_id>/<int:city_id>/<int:materials_id>', views.card, name='card'),
    
]