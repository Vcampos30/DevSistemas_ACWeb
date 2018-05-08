from django.db import models

# Create your models here.
class Aluno(models.Model):
	ra = models.IntegerField("ra")
	nome = models.CharField("nome", max_length=100)
	email = models.EmailField("email", max_length=50)
	def __str__(self):
		return self.nome


		
