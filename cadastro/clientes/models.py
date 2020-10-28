from django.contrib.auth.models import User
from django.db import models


from cadastro.empresas.models import Empresas


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome_razao_social = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=100, blank=True)
    nome_fantasia = models.CharField(max_length=100, blank=True)
    cpf_cnpj = models.CharField(max_length=20, blank=True)
    rg_inscricao_estadual = models.CharField(max_length=15, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=30, blank=True)
    contato = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField('Status', max_length=12, default='ATIVO', blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO'),
        ('INADIMPLENTE', 'INADIMPLENTE'),
    ))
    pessoa = models.CharField(max_length=15, default='JURIDICA', blank=False, null=False, choices=(
        ('JURIDICA', 'JURIDICA'),
        ('FISICA', 'FISICA'),
    ))
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
    data_nascimento_fundacao = models.DateField(blank=True, null=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    logradouro = models.CharField('Logradouro', max_length=50, blank=True)
    numero = models.CharField('Numero', max_length=10, blank=True)
    complemento = models.CharField('Complemento', max_length=30, blank=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True)
    estado = models.CharField('Estado', max_length=2, blank=True)
    observacoes = models.TextField('Observações', max_length=250, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '000' + str(self.id) + ' - ' + self.nome_razao_social

    class Meta:
        db_table = 'clientes'
        ordering = ('nome_razao_social',)
