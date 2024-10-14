from django.urls import path
from .views import index, cadastrar_produto, visualizar_produto, editar_produto

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastrar_produto, name='cadastrar'),
    path('detalhes/<int:pk>/', visualizar_produto, name='det_produto'),
    path('editar/<int:pk>/', editar_produto, name='edit_produto'),
]
