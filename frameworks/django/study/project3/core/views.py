from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class E404View(TemplateView):
    template_name = '404.html'

class E500View(TemplateView):
    template_name = '500.html'