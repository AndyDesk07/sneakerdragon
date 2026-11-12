from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Producto

def index(request):
    # La página principal muestra tres productos destacados.
    destacados = Producto.objects.filter(destacado=True)[:3]
    return render(request, "principal/index.html", {"destacados": destacados})

def urbano(request):
    # Vista de la categoría Urbano: consulta tres productos desde la base de datos.
    productos = Producto.objects.filter(titulo_categoria="Urbano")[:3]
    datos = {
        "titulo": "URBANO",
        "slug": "urbano",
        "categoria": "Urbano",
        "descripcion_categoria": "Sneakers con estilo callejero, cómodos y fáciles de combinar para el uso diario.",
        "productos": productos,
    }
    return render(request, "principal/productos.html", datos)

def deportivo(request):
    # Vista de la categoría Deportivo.
    productos = Producto.objects.filter(titulo_categoria="Deportivo")[:3]
    datos = {
        "titulo": "DEPORTIVO",
        "slug": "deportivo",
        "categoria": "Deportivo",
        "descripcion_categoria": "Modelos pensados para movimiento, entrenamiento y comodidad durante el día.",
        "productos": productos,
    }
    return render(request, "principal/productos.html", datos)


def lujo(request):
    # Vista de la categoría Lujo.
    productos = Producto.objects.filter(titulo_categoria="Lujo")[:3]
    datos = {
        "titulo": "LUJO",
        "slug": "lujo",
        "categoria": "Lujo",
        "descripcion_categoria": "Una selección premium con diseños más exclusivos y una presentación elegante.",
        "productos": productos,
    }
    return render(request, "principal/productos.html", datos)


def detalle_producto(request, producto_id):
    # Busca un producto por su id. Si no existe, Django responde con error 404.
    producto = get_object_or_404(Producto, pk=producto_id)

    rutas_categoria = {
        "Urbano": reverse("urbano"),
        "Deportivo": reverse("deportivo"),
        "Lujo": reverse("lujo"),
    }

    datos = {
        "producto": producto,
        "volver_url": rutas_categoria.get(producto.titulo_categoria, reverse("inicio")),
    }
    return render(request, "principal/detalle_producto.html", datos)
