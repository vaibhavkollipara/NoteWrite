from django.http import HttpResponse
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import AllowAny
from .serializers import *

# Create your views here.


def indexView(request):
    return HttpResponse("Hello")


class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateUpdateSerizalizer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
