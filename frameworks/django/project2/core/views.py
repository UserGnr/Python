from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

# Create your views here.
def index(request):

    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)    # O formulário form pode ser do tipo POST ou None (vazio)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'Assunto: {assunto}')
            print(f'E-mail: {email}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            # prod = form.save(commit=False)

            # print(f'Nome: {prod.nome}')
            # print(f'Preço: {prod.preco}')
            # print(f'Estoque: {prod.estoque}')
            # print(f'Imagem: {prod.imagem}')

            form.save()

            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.erro(request, 'Erro ao salvar o produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)
