from django.shortcuts import render, redirect
from .models import Aluno
from .forms import alunoform

# Create your views here.
def list_alunos(request):
	aluno = Aluno.objects.all()
	return render(request, 'Aluno.html', {'contas': aluno})
	
def create_aluno(request):
	form = alunoform(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('list_alunos')
	return render(request, 'Aluno-Form.html', {'form': form})
	
def update_aluno(request, id):
	aluno = Aluno.objects.get(id=id)
	form = alunoform(request.POST or None, instance=aluno)
	
	if form.is_valid():
		form.save()
		return redirect('list_alunos')
	
	return render(request, 'Aluno-Form.html', {'form':form,'aluno':aluno})
def delete_aluno(request, id):
	aluno = Aluno.objects.get(id=id)
	
	if request.method == 'POST':
		aluno.delete()
		return redirect('list_alunos')
	return render(request, 'Aluno-Delete-Confirma.html', {'aluno': aluno})

