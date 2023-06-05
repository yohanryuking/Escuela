from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("registrar/", registar),
    path("eliminacion/<codigo>", eliminar),
    path("edicion/<codigo>", edicion),
    path("editar/", editar)
]
