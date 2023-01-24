from django.urls import path
from . import views
app_name = "CSV"
urlpatterns = [
    path("", views.index, name='index'),
    path("Conocenos.html", views.conocer, name='conocer'),
    path("Contacto.html", views.contactar, name='contactar'),
    path("index.html", views.inicio, name='inicio'),
    path("InicioDeSesion.html", views.iniciar, name='iniciar'),
    path("Soporte_Remoto.html", views.soporte, name='soporte'),
    path("add", views.add, name="add" ),
    path("login", views.login, name="login" )
]