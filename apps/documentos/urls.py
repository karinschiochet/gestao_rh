from django.urls import path
from .views import (DocumentoCreateView)


urlpatterns = [
    path('create/<int:funcionario_id>/', DocumentoCreateView.as_view(), name='documento_create'),
    #path('create/', DepartamentoCreateView.as_view(), name='departamento_create'),
    #path('update/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    #path('delete/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento_delete'),
]
