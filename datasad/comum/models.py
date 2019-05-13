from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Base(models.Model):

    criado_em = models.DateTimeField('Criado em', auto_now_add=True, blank=False, null=False)

    class Meta:
        abstract = True

    def get_criado_em(self, format):
        return self.criado_em.__format__(format).__str__()

class Perfil(Base):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    sexo = models.CharField('Sexo', max_length=16, choices=SEXO_CHOICES, blank=False, null=False)
    contato = models.CharField('Contato', max_length=16, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=False, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    # foto_perfil = models.ImageField('Foto', upload_to='imagens/%Y/',default='default_foto.png',null=True,blank=True)
    cpf = models.CharField('CPF', max_length=14, null=True)


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return "%s %s" % (self.nome(), self.sobrenome())

    def nome(self):
        return self.usuario.first_name

    def sobrenome(self):
        return self.usuario.last_name
