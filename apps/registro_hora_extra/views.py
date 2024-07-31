from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra

class HoraExtraListView(ListView):
    model = RegistroHoraExtra
    template_name = 'registro_hora_extra/hora_extra_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset