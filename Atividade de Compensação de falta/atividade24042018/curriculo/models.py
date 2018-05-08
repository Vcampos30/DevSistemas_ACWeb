from django.db import models

# Create your models here.

class Disciplina(models.Model):
	nome = models.CharField("nome", max_length=100)
	ementa = models.TextField("ementa")	
	def __str__(self):
		return self.nome
		
class DisciplinaOfertada(models.Model):
	nome_disciplina = models.CharField("nome", max_length=100)
	ano = models.PositiveSmallIntegerField("ano")
	semestre = models.PositiveSmallIntegerField("semestre")
	#disciplina = models.ForeignKey(curriculo.Disciplina, null = True)
	def __str__(self):
		return self.semestre