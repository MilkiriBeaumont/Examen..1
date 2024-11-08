from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


# Vista para listar productos
def index(request):
    productos = Producto.objects.all()
    return render(request, "Registros.html", {'productos': productos})

# Vista para agregar un nuevo producto
def agregar_registro(request):
    if request.method == 'POST':
        try:
            print("Ingresando producto...")

            # Obtener datos del formulario
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria')
            precio = request.POST.get('precio')
            descripcion = request.POST.get('descripcion')
            cantidad_stock = request.POST.get('cantidad_stock')

            # Crear y guardar un nuevo producto
            producto = Producto(
                nombre=nombre,
                categoria=categoria,
                precio=precio,
                descripcion=descripcion,
                cantidad_stock=cantidad_stock
            )
            producto.save()

        except Exception as ex:
            print(f"Error: {ex}")
    
    return redirect('index')

# Vista para eliminar un producto
def eliminar_registro(request, id):
    try:
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
    except Exception as ex:
        print(f"Error: {ex}")

    return redirect('index')

# Vista para actualizar un producto existente
def actualizar_registro(request, id):
    try:
        producto = get_object_or_404(Producto, id=id)
        
        if request.method == 'POST':
            # Actualizar campos del producto
            producto.nombre = request.POST.get('nombre')
            producto.categoria = request.POST.get('categoria')
            producto.precio = request.POST.get('precio')
            producto.descripcion = request.POST.get('descripcion')
            producto.cantidad_stock = request.POST.get('cantidad_stock')
            
            producto.save()
            return redirect('index')
        else:
            productos = Producto.objects.all()
            return render(request, "Registro.html", {'productos': productos, 'producto': producto})

    except Exception as ex:
        print(f"Error: {ex}")
        return redirect('index')



