from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': 'INDEX'
    }

    return render(request, 'index.html', context)


def cadastrar(request):
    context = {
        'titulo': 'CADASTRO'
    }

    return render(request, 'cadastrar.html', context)