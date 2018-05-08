from django import forms
from .models import Disciplina

class disciplinaform(forms.ModelForm):
	class Meta:
		model = Disciplina
		fields = ['nome', 'ementa']