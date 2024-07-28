# Generated by Django 5.0.7 on 2024-07-28 01:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        ('empresas', '0001_initial'),
        ('funcionarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamento',
            field=models.ManyToManyField(to='departamentos.departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]