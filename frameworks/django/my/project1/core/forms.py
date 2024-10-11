from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
        }
