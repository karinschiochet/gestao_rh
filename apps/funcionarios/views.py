from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'funcionarios/funcionario_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']
    template_name = 'funcionarios/funcionario_update.html'

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/funcionario_delete.html'
    success_url = reverse_lazy('funcionario_list')

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']
    template_name = 'funcionarios/funcionario_create.html'
    success_url = reverse_lazy('funcionario_list')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)
