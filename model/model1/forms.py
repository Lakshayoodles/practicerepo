from django import forms
from .models import studentlist


class StudentListForm(forms.ModelForm):
    class Meta:
        model = studentlist
        fields = '__all__'
