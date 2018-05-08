from django import forms
from .models import Atividade

class atividadeform(forms.ModelForm):
	class Meta:
		model = Atividade
		fields = ['titulo', 'data', 'sequencial', 'nome_disciplina','ano','semestre']