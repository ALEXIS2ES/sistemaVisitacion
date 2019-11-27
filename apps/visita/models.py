from django.db import models

# Create your models here.

class Visitador(models.Model):
	nombreCapellan = models.CharField(max_length = 50)
	fecha = models.DateField()
	pdf = models.FileField(upload_to='pdf/', unique=True, blank=True, null=True, default=None)

	class Meta:
		verbose_name ='Visitador'
		verbose_name ='Visitadore'
		ordering = ['nombreCapellan']
	
	def __str__(self):
		return "("+str(self.nombreCapellan)+","+str(self.fecha)+""+str(self.pdf)+")"