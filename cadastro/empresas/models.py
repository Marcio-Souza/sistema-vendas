from django.contrib.auth.models import User
from django.db import models


class Planos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do Plano', max_length=50, blank=False, unique=True)
    descricao = models.TextField('Descrição do Plano', max_length=100, blank=True)
    valor = models.DecimalField('Valor', max_digits=15, blank=False, decimal_places=2, default='0')
    desconto_maximo = models.DecimalField('Desconto Máximo', max_digits=15, blank=False, decimal_places=2, default='0')
    observacoes = models.TextField('Observações', max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Empresas(models.Model):
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField('Razão Social', max_length=50, blank=False, unique=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50, blank=False, unique=False)
    cnpj = models.CharField('CNPJ', max_length=20, blank=False, unique=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=20, blank=True)
    inscricao_municipal = models.CharField('Inscrição Estadual', max_length=20, blank=True)
    contato = models.CharField('Contato', max_length=30, blank=False)
    telefone = models.CharField('Telefone', max_length=30, blank=True)
    celular = models.CharField('Celular', max_length=30, blank=True)
    email = models.EmailField('E-mail', blank=True)
    site = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    logradouro = models.CharField(max_length=40, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=30, blank=False)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    contato_cobranca = models.CharField('Contato', max_length=30, blank=False)
    telefone_cobranca = models.CharField('Telefone', max_length=30, blank=True)
    celular_cobranca = models.CharField('Celular', max_length=30, blank=True)
    email_cobranca = models.EmailField('E-mail cobrança', blank=True)
    logradouro_cobranca = models.CharField(max_length=40, blank=True)
    numero_cobranca = models.CharField(max_length=10, blank=True)
    complemento_cobranca = models.CharField(max_length=30, blank=False)
    bairro_cobranca = models.CharField(max_length=30, blank=True)
    cidade_cobranca = models.CharField(max_length=30, blank=True)
    uf_cobranca = models.CharField(max_length=2, blank=True)
    dia_pagamento = models.IntegerField(blank=True, null=True)
    plano = models.ForeignKey(Planos, on_delete=models.DO_NOTHING)
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=20, blank=False,
                                       choices=(
                                           ('A VISTA', 'A VISTA'),
                                           ('PARCELADO', 'PARCELADO'),
                                           ('FREE', 'FREE'),
                                       ))
    meio_pagamento = models.CharField('Meio de pagamento', max_length=20, blank=False, choices=(
        ('BOLETO BANCARIO', 'BOLETO BANCARIO'),
        ('DINHEIRO EM ESPECIE', 'DINHEIRO EM ESPECIE'),
        ('DEPOSITO EM CONTA', 'DEPOSITO EM CONTA'),
        ('CARTAO DE CREDITO', 'CARTAO DE CREDITO'),
        ('DEBITO EM CONTA', 'DEBITO EM CONTA'),
        ('GRATUIDADE', 'GRATUIDADE'),
        ('OUTROS', 'OUTROS'),
    ))
    status = models.CharField('Status', max_length=20, blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('SUSPENSO', 'SUSPENSO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('NEGATIVADO', 'NEGATIVADO'),
    ))
    data_inicio = models.DateField(blank=True, null=True)
    contrato = models.CharField('Contrato', max_length=30, blank=True)
    observacoes = models.TextField(max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razao_social
