from django.shortcuts import render, redirect
from .forms import VisitadorForm

# Create your views here.

def Home(request):
	return render(request, 'index.html')

def crearVisita(request):
	if request.method == 'POST':
		visita_form = VisitadorForm(request.POST)
		if visita_form.is_valid():
			visita_form.save()
			return redirect('index')
	else:
		visita_form = VisitadorForm()
	return render(request, 'visita/crear_visita.html',{'visita_form' :visita_form})