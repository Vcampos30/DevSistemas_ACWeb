from django import forms
from .models import Aluno

class alunoform(forms.ModelForm):
	class Meta:
		model = Aluno
		fields = ['nome', 'ra', 'email']