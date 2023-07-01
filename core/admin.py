from django.contrib import admin

from core.views import pelicula
from .models import Categoria , Pelicula , Categoriapelicula

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(Categoriapelicula)
