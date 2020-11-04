from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FormularioJuegos
from .models import Juegos

# Create your views here.
def home(request):
    data = {
        'form': FormularioJuegos()
    }
    if request.method == 'POST':
        formulario = FormularioJuegos(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Juego Registrado!"
        else:
            data["form"] = formulario

    return render(request, 'juego/formulariojuego.html', data)
    #def get_success_url(self):
        #return reverse_lazy('login') + '?register'

def principal(request):
    return render(request, 'juego/demo.html')

def proximo(request):
    return render(request, 'juego/proximo.html')

def stock(request):
    return render(request, 'juego/stock.html')

def listar(request):
    print("vista: listar")
    lista = Juegos.objects.all()
    context = {'listado': lista }
    return render(request, 'juego/listar.html', context)

def eliminar(request):
    print("Eliminando producto")
    if request.method == 'POST':
        codigo = request.POST('code')

        if codigo !="":
            try:
                juegos = Juegos()
                juegos = Juegos.objects.get(code=codigo)
                if juegos is not None:
                    print("Nombre del juego", juegos)
                    juegos.delete()

                    return render(request, 'eliminar.html',juegos)