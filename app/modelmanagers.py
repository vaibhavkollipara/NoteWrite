from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager
from .models import *
from .exceptions import *


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.first_name = first_name
        user.last_name = last_name

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class TopicManager(Manager):

    def create_topic(self, user, title):
        topic = Topic()
        topic.user = user
        topic.title = title
        topic.save()


class NoteManager(Manager):

    def create_note(self, topic_id, content):
        try:
            topic = Topic.objects.get(pk=topic_id)
            note = Note()
            note.topic = topic
            note.content = content
            note.save()
        except:
            raise TopicNotFoundException()
