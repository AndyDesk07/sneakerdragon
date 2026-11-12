from django.test import TestCase
from django.urls import reverse

from .models import Producto


class TiendaTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for categoria in ("Urbano", "Deportivo", "Lujo"):
            for numero in range(1, 4):
                Producto.objects.create(
                    titulo_categoria=categoria,
                    nombre=f"Producto {categoria} {numero}",
                    precio=99990,
                    descripcion="Producto de prueba",
                    imagen="principal/images/sneaker-placeholder.svg",
                    stock=5,
                )

    def test_inicio_responde(self):
        self.assertEqual(self.client.get(reverse("inicio")).status_code, 200)

    def test_cada_categoria_muestra_tres_productos(self):
        for ruta in ("urbano", "deportivo", "lujo"):
            respuesta = self.client.get(reverse(ruta))
            self.assertEqual(respuesta.status_code, 200)
            self.assertEqual(len(respuesta.context["productos"]), 3)
