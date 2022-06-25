from django.db import models


# Create your models here.


class Formulario(models.Model):
    ATENDIMENTO = (
        ('LEADS POSITIVO', 'LEADS POSITIVO'),
        ('LEADS NEUTRO', 'LEADS NEUTRO'),
        ('LEADS NEGATIVO', 'LEADS NEGATIVO')

    )

    phone = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=50, null=False, blank=False)
    data = models.DateTimeField(max_length=50, null=False, blank=True)
    anotacoes = models.CharField(blank=True, max_length=255)
    status = models.CharField(blank=True, null=True, choices=ATENDIMENTO, max_length=14)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    nome_pagina = models.CharField(blank=True, null=True, max_length=50)
    whatsapp = models.CharField(blank=True, null=True, max_length=50)
    perfil_facebook = models.URLField(blank=True, null=True, max_length=256)
    perfil_instagram = models.URLField(blank=True, null=True, max_length=256)
    canal_youtube = models.URLField(blank=True, null=True, max_length=256, )

    def __str__(self):
        return self.nome_pagina


class Produto(models.Model):
    nome_produto = models.CharField(blank=False, null=False, max_length=100)
    descricao = models.TextField(blank=False, null=False, max_length=256)
    valor = models.CharField(blank=False, null=False, max_length=11)

    def __str__(self):
        return self.nome_produto


class CadastroClientes(models.Model):
    TIPO = (
        ('CNPJ', 'CNPJ'),
        ('CPF', 'CPF')
    )

    STATUS_CLIENTE = (
        ('ATIVADO', 'ATIVADO'),
        ('DESATIVADO', 'DESATIVADO')
    )

    tipo_juridico = models.CharField(choices=TIPO, blank=False, null=False, max_length=4)
    cnpj = models.CharField(blank=True, null=True, max_length=14)
    nome_empresa = models.CharField(blank=True, null=True, max_length=50)
    cpf = models.CharField(blank=True, null=True, max_length=11)
    nome_usuario = models.CharField(blank=True, null=True, max_length=50)
    ramo_atividade = models.CharField(blank=True, null=True, max_length=50)
    telefone = models.CharField(blank=True, null=True, max_length=13)
    cep = models.CharField(blank=True, null=True, max_length=8)
    endereco = models.CharField(blank=True, null=True, max_length=150)
    num_endereco = models.CharField(blank=True, null=True, max_length=5)
    bairro = models.CharField(blank=True, null=True, max_length=50)
    cidade = models.CharField(blank=True, null=True, max_length=50)
    estado = models.CharField(blank=True, null=True, max_length=50)
    status_cliente = models.CharField(choices=STATUS_CLIENTE, max_length=10)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.nome_empresa is not None:
            return self.nome_empresa
        else:
            return self.nome_usuario
