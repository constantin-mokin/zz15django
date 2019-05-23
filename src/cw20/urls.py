from django.urls import path
from cw20.views import home

urlpatterns = [
    path('home/', home, name='home')
]
