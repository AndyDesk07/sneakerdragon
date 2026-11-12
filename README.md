# SneakerDRAGON

Tienda web de zapatillas desarrollada con Django. El catálogo está organizado en tres categorías: urbano, deportivo y lujo. Este proyecto reúne una interfaz adaptable, vistas de producto y un carrito que conserva sus artículos en el navegador.

## Funcionalidades

- Catálogo de productos destacado y navegación por categoría.
- Páginas con información individual de cada producto.
- Administración de productos desde Django Admin.
- Carrito con cantidades, subtotal y persistencia en `localStorage`.
- Datos de ejemplo cargados mediante migraciones de Django.
- Ilustración de zapatilla original para mostrar el catálogo sin publicar fotografías sin autorización confirmada.

## Tecnologías

- Python 3.10–3.12
- Django 4.2
- SQLite para desarrollo local
- HTML, CSS y JavaScript

## Ejecución local en Windows

Desde PowerShell, en la carpeta del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador. La migración inicial crea el catálogo de demostración en una base SQLite local.

Para administrar el catálogo, crea una cuenta de administrador local y entra en `/admin/`:

```powershell
python manage.py createsuperuser
```

## Configuración para publicación

La clave de Django se configura mediante `DJANGO_SECRET_KEY`. En desarrollo local Django usa una clave de reemplazo; la aplicación exige una clave configurada cuando `DJANGO_DEBUG=False`. Para generar una clave:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
$env:DJANGO_SECRET_KEY = "pega-aqui-la-clave-generada"
$env:DJANGO_DEBUG = "False"
$env:DJANGO_ALLOWED_HOSTS = "tu-dominio.example"
```

Configura estas variables en el servicio de alojamiento; no publiques sus valores en el repositorio.

## Datos excluidos del repositorio

La base de datos SQLite, los archivos `.env`, los entornos virtuales, los archivos generados y las fotografías originales `.jpg` están excluidos por `.gitignore`. El catálogo de demostración utiliza una ilustración de reemplazo original. Cada persona puede crear su propia base local ejecutando las migraciones. No subas bases de datos que contengan cuentas, sesiones o registros de administración.

Si luego agregas fotografías al catálogo, usa imágenes propias o confirma que tienes permiso para publicarlas en GitHub y redistribuirlas.
