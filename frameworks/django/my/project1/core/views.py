from django.shortcuts import render
from .models import Produto
# Create your views here.
def index(request):
    context = {
        'titulo': 'INDEX',
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)


def cadastrar(request):
    context = {
        'titulo': 'CADASTRO',
    }

    return render(request, 'cadastrar.html', context)