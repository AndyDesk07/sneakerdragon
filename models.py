from django.db import models


class Producto(models.Model):
    titulo_categoria = models.CharField(max_length=100, verbose_name="Categoría")
    nombre = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    imagen = models.CharField(max_length=255, blank=True)
    stock = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ["titulo_categoria", "nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    @property
    def precio_formateado(self):
        return f"{self.precio:,}".replace(",", ".")

    def __str__(self):
        return f"{self.nombre} ({self.titulo_categoria})"
