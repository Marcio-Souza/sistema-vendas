from django.contrib.auth.models import User
from django.db import models
from cadastro.empresas.models import Empresas


class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False)
    sobrenome = models.CharField(max_length=50, blank=True)
    rg = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=False, null=False, choices=(
        ('SOLTEIRO', 'SOLTEIRO'),
        ('CASADO', 'CASADO'),
        ('VIUVO', 'VIUVO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('UNIAO ESTAVEL', 'UNIAO ESTAVEL'),
        ('OUTROS', 'OUTROS'),
    ))
    sexo = models.CharField('Sexo', max_length=10, choices=(
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
        ('OUTROS', 'OUTROS'),
    ))
    cep = models.CharField('CEP', max_length=10, blank=True)
    logradouro = models.CharField('Logradouro', max_length=50, blank=True)
    numero = models.CharField('Numero', max_length=10, blank=True)
    complemento = models.CharField('Complemento', max_length=30, blank=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True)
    estado = models.CharField('Estado', max_length=2, blank=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('AFASTADO', 'AFASTADO'),
        ('APOSENTADO', 'APOSENTADO'),
        ('DEMITIDO', 'DEMITIDO'),
    ))
    observacoes = models.TextField('Observações', max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'colaboradores'
        ordering = ('nome',)
