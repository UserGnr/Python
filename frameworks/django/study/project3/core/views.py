# from django.views.generic import TemplateView
# Como tem o forms, vamos usar o FormView
from django.views.generic import FormView
from .models import Servico, Funcionario
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        # order_by('?') é para deixar a order aleatória
        context['funcionarios'] = Funcionario.objects.all()
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.requesto, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    


# class E404View(TemplateView):
#     template_name = '404.html'

# class E500View(TemplateView):
#     template_name = '500.html'

