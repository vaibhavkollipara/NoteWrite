from django.urls import path
from .views import indexView

app_name = 'app'

urlpatterns = [
    path('', indexView, name="index"),
]
