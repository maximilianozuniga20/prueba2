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

def editar(request):
    juego_form = None
    error = None
    try:
        juego = Juegos.objects.get(id = id)
        if request.method == 'GET':
            juego_form = JuegosForm(instance = autor)
        else:
            juego_form = JuegosForm(request.POST, instance = autor)
            if juego_form.is_valid():
                juego_form.save()
            return redirect('index')
        except ObjectDoesNotExist as e:
            error = e
        return render(request,'juego/listar.html', {'juego_form':juego_form,'error':error})

def eliminar(request):
    juego = Juegos.objects.get(id = id)
    juego.delete()
    return redirect('juegos:listar')