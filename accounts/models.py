from django.db import models
from django.contrib import auth

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Client(auth.models.User,auth.models.PermissionsMixin):

    name = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='client_name',null=True,blank=True)

    def __str__(self):
        return "@{}".format(self.username) + "-" + self.first_name + " " + self.last_name
