from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="inicio"),
    path("urbano/", views.urbano, name="urbano"),
    path("deportivo/", views.deportivo, name="deportivo"),
    path("lujo/", views.lujo, name="lujo"),
    path("producto/<int:producto_id>/", views.detalle_producto, name="detalle_producto"),
]
