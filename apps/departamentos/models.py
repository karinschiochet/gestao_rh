from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    def get_absolute_url(self):
        return reverse('departamento_list')

    def __str__(self):
        return self.nome
