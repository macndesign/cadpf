from django.db import models


class Cadastro(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField('Nome', max_length=200)
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO_CHOICES)

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'
        ordering = ['nome']

    def __str__(self):
        return self.nome
