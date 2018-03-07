from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .modelmanagers import *


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    class Meta:
        db_table = 'users'


class Topic(models.Model):

    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'topics'
        ordering = ['-created']


class Notes(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __view(self):
        if len(self.content) < 10:
            return self.content
        else:
            return "{}...".format(self.content[:6])

    def __str__(self):
        return self.__view()

    def __repr__(self):
        return self.__view()

    class Meta:
        db_table = 'notes'
        ordering = ['-created']
