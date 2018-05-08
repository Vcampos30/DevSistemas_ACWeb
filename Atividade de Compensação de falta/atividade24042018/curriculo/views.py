from django.shortcuts import render, redirect
from .models import Disciplina
from .forms import disciplinaform

# Create your views here.
def list_disciplinas(request):
	disciplina = Disciplina.objects.all()
	return render(request, 'Disciplina.html', {'curriculo': disciplina})
	
def create_disciplina(request):
	form = disciplinaform(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('list_disciplinas')
	return render(request, 'Disciplina-Form.html', {'form': form})
	
def update_disciplina(request, id):
	disciplina = Disciplina.objects.get(id=id)
	form = disciplinaform(request.POST or None, instance=disciplina)
	
	if form.is_valid():
		form.save()
		return redirect('list_disciplinas')
	
	return render(request, 'Disciplina-Form.html', {'form':form,'disciplina':disciplina})
def delete_disciplina(request, id):
	disciplina = Disciplina.objects.get(id=id)
	
	if request.method == 'POST':
		disciplina.delete()
		return redirect('list_disciplinas')
	return render(request, 'Disciplina-Delete-Confirma.html', {'disciplina': disciplina})
