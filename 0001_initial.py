from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo_categoria", models.CharField(max_length=100, verbose_name="Categoría")),
                ("nombre", models.CharField(max_length=200)),
                ("precio", models.PositiveIntegerField(default=0)),
                ("descripcion", models.TextField(blank=True)),
                ("imagen", models.CharField(blank=True, max_length=255)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("destacado", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
                "ordering": ["titulo_categoria", "nombre"],
            },
        ),
    ]
