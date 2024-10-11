from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def index(request):
    context = {
        'titulo': 'INDEX',
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)


def cadastrar_produto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()

    context = {
        'titulo': 'CADASTRO',
        'formulario': form,
    }

    return render(request, 'cadastrar.html', context)