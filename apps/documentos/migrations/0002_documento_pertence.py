# Generated by Django 5.0.7 on 2024-07-28 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.funcionario'),
        ),
    ]