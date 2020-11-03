from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Inicio de Sesion"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

def principal(request):
    return render(request, 'juego/demo.html')

def proximo(request):
    return render(request, 'juego/proximo.html')

def stock(request):
    return render(request, 'juego/stock.html')