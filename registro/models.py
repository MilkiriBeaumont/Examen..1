from django.db import models

class Producto(models.Model):

    nombre = models.CharField(max_length=100,default=False)               # Nombre del producto
    categoria = models.CharField(max_length=50,default=False)             # Categoría del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=False)  # Precio del producto
    descripcion = models.TextField(default=False)                        # Descripción del producto
    cantidad_stock = models.IntegerField(default=False)                  # Cantidad en stock
   
    



    def __str__(self):
        return self.nombre
