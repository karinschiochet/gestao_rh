from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Empresa
from django.http import HttpResponse
class EmpresaCreateView(CreateView):
    model = Empresa
    template_name = 'empresas/empresa_create.html'
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Usuário vinculado')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nome']
    template_name = 'empresas/empresa_update.html'
