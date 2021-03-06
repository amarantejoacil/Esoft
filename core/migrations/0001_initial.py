# Generated by Django 4.0.5 on 2022-06-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('numero_endereco', models.IntegerField(verbose_name='Número de endereço:')),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
