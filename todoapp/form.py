from .models import Task
from django import forms 

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','complete']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class':'form-control','class':'form-check-label'}),
            'create':forms.DateTimeInput(attrs={'class':'form-control'})
        }
        



