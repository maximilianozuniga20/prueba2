from django.urls import path
from .views import HomePageView, SamplePageView
from .views import principal, proximo, stock

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('principal/', principal, name="principal"),
    path('proximo/', proximo, name="proximo"),
    path('stock/', stock, name="stock"),
]