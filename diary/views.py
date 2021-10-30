from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from .models import Diary_Note
from .forms import Diary_Note_Form
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime

# Create your views here.

def welcome(request):
    return render(request,'diary/welcome.html')
    
@login_required
def create_a_log(request):
    form = Diary_Note_Form
    context = {
        'form' : form
    }
    return render(request, 'diary/create.html' ,context)
@login_required
def save_log(request):
    form = Diary_Note_Form(request.POST)
    
    
    if form.is_valid():
        # save the form data to model
        Pre_Diary_Note = form.save(commit=False)
        Pre_Diary_Note.Owner = request.user
        Pre_Diary_Note.save()

        return HttpResponseRedirect(reverse('diary:welcome'))

    else:
        return HttpResponse('Invaild')


@login_required
def show_diary(request):
    diary_notes = Diary_Note.objects.filter(Owner=request.user)
    
    dates = []
    for note in diary_notes:
        date = note.created_date.date()
        dates.append(date)
    dates = list(set(dates))
    context = {
        'dates':dates,
    }
    print(dates)

    return render(request,'diary/mydiary.html',context=context) 

    
@login_required
def show_date(request,year,month,day):
    day_notes  = Diary_Note.objects.filter(Owner=request.user,
                                            created_date__year = year,
                                            created_date__month = month,
                                            created_date__day = day, )

    return render(request,'diary/day.html',{'day_notes':day_notes})

@login_required
def show_note(request,id):
    note  = Diary_Note.objects.filter(Owner=request.user,id=id)

    context = {
        'note': note,
       

    }
    return render(request,'diary/note.html',context)