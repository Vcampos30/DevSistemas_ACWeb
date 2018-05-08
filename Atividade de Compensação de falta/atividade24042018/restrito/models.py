from django.db import models

# Create your models here.

class Atividade(models.Model):
	nome_disciplina = models.CharField("nome", max_length=100)
	ano = models.PositiveSmallIntegerField("ano")
	semestre = models.PositiveSmallIntegerField("semestre")
	sequencial = models.PositiveSmallIntegerField("sequencial")
	titulo = models.CharField("titulo",max_length=150)
	data = models.DateField("data")
	#disciplinaofertada = models.ForeignKey(curriculo.DisciplinaOfertada, null = True)
	
	def __str__(self):
		return self.titulo
		
class AlunoAtividade(models.Model):
	ra_atividade = models.IntegerField("ra")
	nome_disciplina = models.CharField("nome", max_length=100)
	ano = models.PositiveSmallIntegerField("ano")
	semestre = models.PositiveSmallIntegerField("semestre")
	sequencial = models.PositiveSmallIntegerField("sequencial")
	nota = models.DecimalField("nota",max_digits=4,decimal_places=2)
	#atividade = models.ForeignKey(contas.Atividade, null=True)
	#atividade = models.ForeignKey(restrito.Atividade, null  = True)
	
	def __str__(self):
		return self.nota
		
class Matricula(models.Model):
	ra_atividade = models.IntegerField("ra")
	nome_disciplina = models.CharField("nome", max_length=100)
	ano = models.PositiveSmallIntegerField("ano")
	semestre = models.PositiveSmallIntegerField("semestre")
	#atividade = models.ForeignKey(contas.Atividade, null=True)
	#disciplinaofertada = models.ForeignKey(curriculo.DisciplinaOfertada, null = True)
	def __str__(self):
		return self.ano