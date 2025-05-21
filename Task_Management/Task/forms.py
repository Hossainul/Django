from django import forms
from .models import AddTask

class formTask(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = '__all__'

        widgets = {
            'assigndate' : forms.DateInput(attrs={'type' : 'datetime-local'}),
            'iscomplete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'tasktitle' : 'Task Title',
            'taskdescription' : 'Task Description',
            'iscomplete' : 'is complete ?',
            'assigndate' : 'Assign Date',
            
        }