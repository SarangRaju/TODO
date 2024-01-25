from . models import Tasks
from django import forms
class todoform(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['name','priority','date']