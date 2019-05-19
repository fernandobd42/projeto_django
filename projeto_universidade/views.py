from django.shortcuts import render, redirect
from .models import Universidade, Endereco, Curso
from .forms import UniversidadeForm, EnderecoForm, CursoForm

# Create your views here.
def index(request):
   return render(request, 'index.html')


# Universidades
def universidades(request):
  universidades = Universidade.objects.all()
  return render(request, 'universidades.html', {'universidades': universidades})

def cadastrar_universidade(request):
  form = UniversidadeForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('universidades')
  return render(request, 'universidade.html', {'form': form})

def editar_universidade(request, codigo):
  universidade = Universidade.objects.get(id=codigo)
  form = UniversidadeForm(request.POST or None, instance=universidade)
  if form.is_valid():
    form.save()
    return redirect('universidades')
  return render(request, 'universidade.html', {'form': form, 'universidade': universidade})

def visualizar_universidade(request, codigo):
  universidade = Universidade.objects.get(id=codigo)
  return render(request, 'universidade.html', {'universidade': universidade})

def excluir_universidade(request, codigo):
  universidade = Universidade.objects.get(id=codigo)
  if request.method == 'POST':
    universidade.delete()
    return redirect('universidades')
  return render(request, 'universidade.html', {'universidade': universidade})


# Enderecos
def enderecos(request):
  enderecos = Endereco.objects.all()
  return render(request, 'enderecos.html', {'enderecos': enderecos})

def cadastrar_endereco(request):
  form = EnderecoForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('enderecos')
  return render(request, 'endereco.html', {'form': form})

def editar_endereco(request, codigo):
  endereco = Endereco.objects.get(id=codigo)
  form = EnderecoForm(request.POST or None, instance=endereco)
  if form.is_valid():
    form.save()
    return redirect('enderecos')
  return render(request, 'endereco.html', {'form': form, 'endereco': endereco})

def visualizar_endereco(request, codigo):
  endereco = Endereco.objects.get(id=codigo)
  return render(request, 'endereco.html', {'endereco': endereco})

def excluir_endereco(request, codigo):
  endereco = Endereco.objects.get(id=codigo)
  if request.method == 'POST':
    endereco.delete()
    return redirect('enderecos')
  return render(request, 'endereco.html', {'endereco': endereco})


  # Cursos
def cursos(request):
  cursos = Curso.objects.all()
  return render(request, 'cursos.html', {'cursos': cursos})

def cadastrar_curso(request):
  form = CursoForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('cursos')
  return render(request, 'curso.html', {'form': form})

def editar_curso(request, codigo):
  curso = Curso.objects.get(id=codigo)
  form = CursoForm(request.POST or None, instance=curso)
  if form.is_valid():
    form.save()
    return redirect('cursos')
  return render(request, 'curso.html', {'form': form, 'curso': curso})

def visualizar_curso(request, codigo):
  curso = Curso.objects.get(id=codigo)
  return render(request, 'curso.html', {'curso': curso})

def excluir_curso(request, codigo):
  curso = Curso.objects.get(id=codigo)
  if request.method == 'POST':
    Curso.delete()
    return redirect('cursos')
  return render(request, 'curso.html', {'curso': curso})