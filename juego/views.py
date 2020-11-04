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

def edit(request, id_juego):
    juego = Juegos.objects.filter(id=id_juego).first()
    form = FormularioJuegos(instance=juego)
    return render(request, "juego/JuegoEdit.html", {"form":form, "juego":juego} )

def actualizar_juego(request, id_juego):
    juego = Juegos.objects.get(pk=id_juego)
    form = FormularioJuegos(request.POST, instance=juego)
    if form.is_valid():
        form.save()
    juegos = Juegos.objects.all()
    return render(request, "juego/listar.html", {"juegos":juegos} )

def eliminar(request, id_juego):
    juego = Juegos.objects.get(pk = id_juego)
    juego.delete()
    juegos = Juegos.objects.all()
    return render(request, 'juego/listar.html', {'juegos':juegos, "mensaje":'OK'})