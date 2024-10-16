from django.shortcuts import render, redirect, get_object_or_404
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
        form = ProdutoForm(request.POST, request.FILES)
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

def visualizar_produto(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    context = {
        'titulo': 'Detalhe',
        'produto': produto,
    }
    return render(request, 'detalhe_produto.html', context)

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance = produto)    # Preenche o form com os dados do produto
        if form.is_valid():
            form.save()
            return redirect ('det_produto', pk = produto.id)
    else:
        form = ProdutoForm(instance=produto)    # Exibe o formulário com os dados atuais do produto

    context = {
        'titulo': 'Editar',
        'form': form,
        'produto': produto,
    }

    return render(request, 'editar_produto.html', context)

