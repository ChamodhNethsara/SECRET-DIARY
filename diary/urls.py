from django.urls import path
from .views import *
app_name= 'diary'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('create',create_a_log,name='create_log'),
    path('save',save_log,name='save_log'),

    path('diary',show_diary,name='show_diary'),
    path('show_date/<int:year>/<int:month>/<int:day>/',show_date,name='show_date'),
    path('show_note/<int:id>/',show_note,name='show_note'),


]