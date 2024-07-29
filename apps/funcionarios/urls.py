from django.urls import path
from .views import FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView, FuncionarioCreateView

urlpatterns = [
    path('create/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('list/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('update/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete'),

]
