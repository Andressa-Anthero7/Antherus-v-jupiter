# Generated by Django 4.0.3 on 2022-05-25 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('data', models.DateTimeField(blank=True, max_length=50)),
                ('anotacoes', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, choices=[('LEADS POSITIVO', 'LEADS POSITIVO'), ('LEADS NEUTRO', 'LEADS NEUTRO'), ('LEADS NEGATIVO', 'LEADS NEGATIVO')], max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pagina', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=50, null=True)),
                ('perfil_facebook', models.URLField(blank=True, max_length=256, null=True)),
                ('perfil_instagram', models.URLField(blank=True, max_length=256, null=True)),
                ('canal_youtube', models.URLField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=256)),
                ('valor', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_juridico', models.CharField(choices=[('CNPJ', 'CNPJ'), ('CPF', 'CPF')], max_length=4)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('nome_empresa', models.CharField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('nome_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('ramo_atividade', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=13, null=True)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('endereco', models.CharField(blank=True, max_length=150, null=True)),
                ('num_endereco', models.CharField(blank=True, max_length=5, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('status_cliente', models.CharField(choices=[('ATIVADO', 'ATIVADO'), ('DESATIVADO', 'DESATIVADO')], max_length=10)),
                ('data_contratacao', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.produto')),
            ],
        ),
    ]
