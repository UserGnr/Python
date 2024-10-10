from django.urls import path
from .views import index, cadastrar


urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastrar, name='cadastrar')
]
