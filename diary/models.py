from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.






class Diary_Note(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Body  = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.Title

    def get_more_url(self):
        return reverse('diary:show_note',kwargs={'id':self.id})


        
