from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('signup/', UserCreateApiView.as_view(), name="signup"),
]
