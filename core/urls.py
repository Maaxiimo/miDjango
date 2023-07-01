from django.urls import path


import core
from .views import index, lomasnuevo, recomendadas , ranking, categoria , pelicula , peliculasmostrar , registrarpelicula , editarpeliculas ,eliminarpeliculas
urlpatterns = [
    path('', index, name="index"),
    path('lomasnuevo', lomasnuevo, name="lomasnuevo"),
    path('recomendadas', recomendadas, name="recomendadas"),
    path('ranking', ranking, name="ranking"),
    path('categoria/<int:id>', categoria, name="categoria"),
    path('pelicula/<int:id>', pelicula, name="pelicula"),
    path('peliculasmostrar', peliculasmostrar , name = "peliculasmostrar"),
    path('registrar' , registrarpelicula , name = "registrar" ),
    path('editarpeliculas' , editarpeliculas , name = "editarpeliculas" ),
     path('eliminarpeliculas/<int:id>',eliminarpeliculas , name="eliminarpeliculas"),
]