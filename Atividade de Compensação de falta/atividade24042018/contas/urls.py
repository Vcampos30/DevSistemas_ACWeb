from django.urls import path
from .views import list_alunos, create_aluno, update_aluno, delete_aluno

urlpatterns = [
	path('', list_alunos, name='list_alunos'),
	path('new', create_aluno, name='create_aluno'),
	path('update/<int:id>', update_aluno, name='update_aluno'),
	path('delete/<int:id>', delete_aluno, name='delete_aluno'),
]