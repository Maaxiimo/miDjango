from multiprocessing import context
from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Categoria, Categoriapelicula , Pelicula 

# Create your views here.
def index (request):
    categorias = Categoria.objects.all()
    contexto = {"categ": categorias}
    return render(request , 'core/index.html',contexto)
def lomasnuevo (request):
    categorias = Categoria.objects.all()
    contexto = {"categ": categorias}
    return render (request , 'core/lomasnuevo.html',contexto)

def recomendadas (request):
    categorias = Categoria.objects.all()
    contexto = {"categ": categorias}
    return render (request , 'core/recomendadas.html',contexto)

def ranking (request):
    categorias = Categoria.objects.all()
    contexto = {"categ": categorias}
    return render (request , 'core/ranking.html',contexto)

def categoria(request,id):

    categorias = Categoria.objects.all()
    if (id == 0):
        peliculas = Categoriapelicula.objects.all()
    else:
        categ = Categoria.objects.get(  idcategoria = id)
        peliculas = Categoriapelicula.objects.filter( categoria = categ)

    contexto = {"categ": categorias, "peli":peliculas}
    
    return render(request,'core/categoria.html',contexto)

def pelicula (request , id):
    peliculas = Pelicula.objects.get(idpelicula = id)
    categ = Categoriapelicula.objects.filter(pelicula = peliculas)
    contexto = {"cat": categ, "peli":peliculas}
    return render(request,'core/pelicula.html', contexto)

def peliculasmostrar (request):
    peliculas = Categoriapelicula.objects.all()
    contexto = {"peli":peliculas}
    return render(request , 'core/peliculasmostrar.html',contexto)  

def registrarpelicula(request):
    nombrepelicula = request.POST['nombrepelicula']
    director= request.POST['director']
    reparto = request.POST['reparto']
    descripcion = request.POST['descripcion']
    imagen = request.FILES['imagen']
    #obtener el registro completo de la raza

    #insert
    pelicula.objects.create(nombrepelicula = nombrepelicula, director = director, reparto = reparto, descripcion = descripcion ,imagen = imagen ) 

    messages.success(request,'Pelicula Registrada')

def editarpeliculas(request):
    return  render  (request , 'core/editarpelicula.html')


def eliminarpeliculas( request , id):
    pelicula1 = Pelicula.objects.get(idpelicula = id)
    pelicula1.delete() 
    messages.success(request,'pelicula Eliminada')
    return redirect('peliculasmostrar')