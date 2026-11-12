from django.db import migrations


PRODUCTOS = [
    # URBANO
    {
        "titulo_categoria": "Urbano",
        "nombre": "Nike Shox TL Triple Black",
        "precio": 169990,
        "descripcion": "Zapatilla urbana en tonos negros, con una silueta llamativa y cómoda para uso diario.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 8,
        "destacado": True,
    },
    {
        "titulo_categoria": "Urbano",
        "nombre": "Air Jordan 1 Retro High",
        "precio": 159990,
        "descripcion": "Modelo de caña alta con estilo callejero, ideal para combinar con looks urbanos.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 6,
        "destacado": False,
    },
    {
        "titulo_categoria": "Urbano",
        "nombre": "Adidas Superstar Street",
        "precio": 79990,
        "descripcion": "Un modelo clásico y fácil de combinar, pensado para un estilo urbano más limpio.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 12,
        "destacado": False,
    },
    # DEPORTIVO
    {
        "titulo_categoria": "Deportivo",
        "nombre": "Runner Black Pro",
        "precio": 119990,
        "descripcion": "Modelo liviano para entrenamiento y caminatas, con una base cómoda y estable.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 10,
        "destacado": False,
    },
    {
        "titulo_categoria": "Deportivo",
        "nombre": "Court Red Performance",
        "precio": 109990,
        "descripcion": "Diseño deportivo de caña media con buen soporte y un look inspirado en el básquetbol.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 7,
        "destacado": True,
    },
    {
        "titulo_categoria": "Deportivo",
        "nombre": "Sprint White Boost",
        "precio": 99990,
        "descripcion": "Zapatilla deportiva clara y versátil, ideal para actividad física de intensidad moderada.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 9,
        "destacado": False,
    },
    # LUJO / PREMIUM
    {
        "titulo_categoria": "Lujo",
        "nombre": "Dragon Black Limited",
        "precio": 229990,
        "descripcion": "Edición premium en negro, presentada como una alternativa exclusiva dentro del catálogo.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 4,
        "destacado": False,
    },
    {
        "titulo_categoria": "Lujo",
        "nombre": "Heritage Red Premium",
        "precio": 249990,
        "descripcion": "Modelo premium de caña alta, con una apariencia clásica y una presentación más exclusiva.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 3,
        "destacado": False,
    },
    {
        "titulo_categoria": "Lujo",
        "nombre": "Icon White Leather",
        "precio": 199990,
        "descripcion": "Diseño blanco de estilo minimalista, pensado para una sección de zapatillas premium.",
        "imagen": "principal/images/sneaker-placeholder.svg",
        "stock": 5,
        "destacado": True,
    },
]


def cargar_productos(apps, schema_editor):
    Producto = apps.get_model("principal", "Producto")
    for datos in PRODUCTOS:
        Producto.objects.update_or_create(nombre=datos["nombre"], defaults=datos)


def eliminar_productos(apps, schema_editor):
    Producto = apps.get_model("principal", "Producto")
    Producto.objects.filter(nombre__in=[p["nombre"] for p in PRODUCTOS]).delete()


class Migration(migrations.Migration):
    dependencies = [("principal", "0001_initial")]

    operations = [migrations.RunPython(cargar_productos, eliminar_productos)]
