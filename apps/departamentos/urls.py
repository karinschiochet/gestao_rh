from django.urls import path
from .views import (
    DepartamentoListView,
    DepartamentoCreateView,
    DepartamentoUpdateView,
    DepartamentoDeleteView
)


urlpatterns = [
    path('list/', DepartamentoListView.as_view(), name='departamento_list'),
    path('create/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('update/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('delete/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento_delete'),
]
