from django.db import models

# Create your models here.
class Flores(models.Model):

    id = models.IntegerField(primary_key=1)
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    descricao = models.CharField(max_length=100)
    preco = models.FloatField(max_length=100)


def __str__(self):
    return self.id