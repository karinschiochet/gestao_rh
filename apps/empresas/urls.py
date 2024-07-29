from django.urls import path
from .views import EmpresaCreateView, EmpresaUpdateView

urlpatterns = [
    path('create/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('update/<int:pk>', EmpresaUpdateView.as_view(), name='empresa_edit'),
]
