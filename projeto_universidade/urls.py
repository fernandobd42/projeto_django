from django.urls import path

from .views import index, universidades, visualizar_universidade, cadastrar_universidade, editar_universidade, excluir_universidade, enderecos, visualizar_endereco, cadastrar_endereco, editar_endereco, excluir_endereco, cursos, visualizar_curso, cadastrar_curso, editar_curso, excluir_curso

urlpatterns = [
  path('', index, name="index"),
  path('universidades', universidades, name='universidades'),
  path('visualizar-universidade/<int:codigo>', visualizar_universidade, name='visualizar-universidade'),
  path('cadastrar-universidade', cadastrar_universidade, name='cadastrar-universidade'),
  path('editar-universidade/<int:codigo>', editar_universidade, name='editar-universidade'),
  path('excluir-universidade/<int:codigo>', excluir_universidade, name='excluir-universidade'),
  path('enderecos', enderecos, name='enderecos'),
  path('visualizar-endereco/<int:codigo>', visualizar_endereco, name='visualizar-endereco'),
  path('cadastrar-endereco', cadastrar_endereco, name='cadastrar-endereco'),
  path('editar-endereco/<int:codigo>', editar_endereco, name='editar-endereco'),
  path('excluir-endereco/<int:codigo>', excluir_endereco, name='excluir-endereco'),
  path('cursos', cursos, name='cursos'),
  path('visualizar-curso/<int:codigo>', visualizar_curso, name='visualizar-curso'),
  path('cadastrar-curso', cadastrar_curso, name='cadastrar-curso'),
  path('editar-curso/<int:codigo>', editar_curso, name='editar-curso'),
  path('excluir-curso/<int:codigo>', excluir_curso, name='excluir-curso'),
]