from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    Serializer
)

from .models import *


class UserCreateUpdateSerizalizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        return User.objects.create_user(first_name, last_name, email, password)


class TopicListCreateSerializer(ModelSerializer):
    notes = SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'notes', 'created', 'updated']

    def create(self, validated_data):
        user = validated_data['user']
        title = validated_data['title']
        return Topic.objects.create_topic(user, title)

    def get_notes(self, obj):
        return obj.notes_set.count()


class NotesListCreateSerializer(ModelSerializer):

    class Meta:
        model = Notes
        fields = ['id','content','created','updated']
