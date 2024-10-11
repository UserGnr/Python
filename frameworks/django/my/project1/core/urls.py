from django.urls import path
from .views import index, cadastrar_produto

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastrar_produto, name='cadastrar'),
]
