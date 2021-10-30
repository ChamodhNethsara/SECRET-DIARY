from django.contrib.auth import login
from django.urls import include,path


app_name = 'accounts'

urlpatterns = [
    path('',include('django.contrib.auth.urls'))
]