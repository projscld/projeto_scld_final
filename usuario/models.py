from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField('Nome completo', max_length=100, null=False, blank=False)
    email = models.EmailField('E-mail institucional', null=False, blank=False)
    turma = models.IntegerField('Turma', null=False, blank=False)
    curso = models.CharField('Curso', max_length=25, null=False, blank=False)
    senha = models.CharField('Senha', max_length=12, null=False, blank=False)
    
    def __str__(self):
        return self.nome
