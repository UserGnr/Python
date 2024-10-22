from django.views.generic import TemplateView
from .models import Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        # order_by('?') é para deixar a order aleatória
        context['funcionarios'] = Funcionario.objects.all()
        return context

class E404View(TemplateView):
    template_name = '404.html'

class E500View(TemplateView):
    template_name = '500.html'

