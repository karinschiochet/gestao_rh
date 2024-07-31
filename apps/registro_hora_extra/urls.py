from django.urls import path
from .views import (
     HoraExtraListView,
#     FuncionarioUpdateView,
#     FuncionarioDeleteView,
#     FuncionarioCreateView,
)

urlpatterns = [
    path('create/', HoraExtraListView.as_view(), name='hora_extra_list'),
    # path('list/', FuncionarioListView.as_view(), name='funcionario_list'),
    # path('update/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),
    # path('delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete'),

]
