from django.urls import path
from .views import list_atividades, create_atividade, update_atividade, delete_atividade

urlpatterns = [
	path('', list_atividades, name='list_atividades'),
	path('new', create_atividade, name='create_atividade'),
	path('update/<int:id>', update_atividade, name='update_atividade'),
	path('delete/<int:id>', delete_atividade, name='delete_atividade'),
]