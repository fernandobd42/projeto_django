from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Endereco(models.Model):
  rua = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
  bairro = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
  numero = models.IntegerField(validators=[MinValueValidator(0)])
  estado = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
  cidade = models.CharField(max_length=100, validators=[MinLengthValidator(3)])

  def __str__(self):
    return self.estado + ' - ' + self.cidade + ' ( ' + self.rua + ' - ' + self.bairro + ' ) ';


class Curso(models.Model):
  nome = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
  area = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
  notaMEC = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

  def __str__(self):
    return self.nome + ' - ' + self.area;
    

class Universidade(models.Model):
  nome = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
  sigla = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
  descricao = models.TextField(validators=[MinLengthValidator(5)])
  endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
  cursos = models.ManyToManyField(Curso)

  def __str__(self):
    return self.nome + ' - ' + self.sigla;
