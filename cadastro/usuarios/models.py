from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=30, blank=False, null=True)
    sobre_nome = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    status = models.CharField('Status', max_length=10, default='ATIVO', blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO')
    ))
    observacoes = models.TextField(max_length=200, blank=True, null=True)
    model_template = models.CharField(max_length=100, blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'
        ordering = ('nome',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        senha = self.email.replace('.', '').replace('@', '')
        if not self.pk:
            user = User.objects.filter(username=self.email)
            if not user.count():
                user = User.objects.create_user(self.email, self.email, senha)
                user.save()
            self.usuario = user
        else:
            self.usuario = self.email
            self.usuario.email = self.email
        super(Usuarios, self).save()
