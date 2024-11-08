from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vista para listar productos
    path('agregar_registro', views.agregar_registro, name='agregar_registro'),  # Vista para agregar un nuevo producto
    path('eliminar_registro/<int:id>', views.eliminar_registro, name='eliminar_registro'),  # Vista para eliminar un producto
    path('actualizar_registro/<int:id>', views.actualizar_registro, name='actualizar_registro')  # Vista para actualizar un producto
]
