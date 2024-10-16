from django.urls import path
from .views import index, cadastrar_produto, visualizar_produto, editar_produto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastrar_produto, name='cadastrar'),
    path('detalhes/<int:pk>/', visualizar_produto, name='det_produto'),
    path('editar/<int:pk>/', editar_produto, name='edit_produto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    