from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('edit_type/<int:id>', views.edit_type, name = 'edit_type'),
    path('edit_technic/<int:id>', views.edit_technic, name = 'edit_technic'),
    path('create_technic', views.create_technic, name = "create_technic")
]