
from django import forms
from .models import Diary_Note
from ckeditor.fields import RichTextFormField

class Diary_Note_Form(forms.ModelForm):
    class Meta:
        model = Diary_Note
        fields = ['created_date','Title','Body']

        labels = {
            'created_date':'Created On',
            'Title':'Title',
            'Body': 'Body',
        }
        
        widgets = {
            'created_date': forms.DateTimeInput(attrs={
                'class':'form-control',
                'readonly':'True',
                }) ,
            'Title' : forms.TextInput(attrs={
                'class':'form-control'
                }),
            'Body': forms.Textarea(attrs={
                'class':'form-control django-ckeditor-widget ckeditor',
                'id':'form-control',
                'spellcheck':'False'}),
        }