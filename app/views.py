from django.http import HttpResponse
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import AllowAny
from .serializers import *


def index(request):
    html = """
        <center><h2>NoteWrite</h1></center>
        <h4>Api Endpoints</h4>
        <ul>
            <li>/api/signup/</li>
        </ul>
        <h4>Authentication</h4>
        <ul>
            <li>/auth/obtaintoken/</li>
            <li>/auth/verifytoken/</li>
            <li>/auth/refreshtoken/</li>
        </ul>
    """
    return HttpResponse(html)


class UserCreateApiView(CreateAPIView):
    """
    Api view to signup new user
    """
    serializer_class = UserCreateUpdateSerizalizer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class TopicListCreateApiView(ListCreateAPIView):
    """
    Api view to create new topic
    """
    serializer_class = TopicListCreateSerializer

    def get_queryset(self, *args, **kwargs):
        return self.request.user.topic_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
