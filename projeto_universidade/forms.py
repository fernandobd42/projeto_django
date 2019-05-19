from django import forms
from .models import Universidade, Endereco, Curso

class UniversidadeForm(forms.ModelForm):
  class Meta:
    model = Universidade
    fields = { 'nome', 'sigla', 'descricao', 'endereco', 'cursos'}

class EnderecoForm(forms.ModelForm):
  class Meta:
    model = Endereco
    fields = { 'rua', 'bairro', 'numero', 'estado', 'cidade'}

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = { 'nome', 'area', 'notaMEC'}