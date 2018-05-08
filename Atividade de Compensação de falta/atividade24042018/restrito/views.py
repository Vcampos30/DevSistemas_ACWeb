from django.shortcuts import render, redirect
from .models import Atividade
from .forms import atividadeform

# Create your views here.
def list_atividades(request):
	atividade = Atividade.objects.all()
	return render(request, 'Atividade.html', {'restrito': atividade})
	
def create_atividade(request):
	form = atividadeform(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('list_atividades')
	return render(request, 'Atividade-Form.html', {'form': form})
	
def update_atividade(request, id):
	atividade = Atividade.objects.get(id=id)
	form = atividadeform(request.POST or None, instance=atividade)
	
	if form.is_valid():
		form.save()
		return redirect('list_atividades')
	
	return render(request, 'Atividade-Form.html', {'form':form,'atividade':atividade})
def delete_atividade(request, id):
	atividade = Atividade.objects.get(id=id)
	
	if request.method == 'POST':
		atividade.delete()
		return redirect('list_atividades')
	return render(request, 'Atividade-Delete-Confirma.html', {'atividade': atividade})
