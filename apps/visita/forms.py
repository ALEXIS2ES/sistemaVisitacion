from django import forms
from .models import Visitador

class VisitadorForm(forms.ModelForm):
	class Meta:
		model = Visitador
		fields = ['nombreCapellan','fecha','pdf']
	