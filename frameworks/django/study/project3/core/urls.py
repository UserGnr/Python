from django.urls import path
from .views import IndexView, E404View, E500View

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # path("E404/", E404View.as_view(), name="E404"),
    # path("E500/", E500View.as_view(), name="E500"),
    # As novas versões do django não precisam criar as páginas de erro dessa forma, basta ter um template nomeado com o erro 404 e 500, por exemplo
]
