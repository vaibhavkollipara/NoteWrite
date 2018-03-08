from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('signup/', UserCreateApiView.as_view(), name="signup"),
    path('topics/', TopicListCreateApiView.as_view(), name="listcreatetopic"),
    path('topics/<int:id>/', TopicUpdateApiView.as_view(), name="updateDeletetopic"),

]
