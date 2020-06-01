from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from uuid import uuid4

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**kwargs):
        user = self.model(email=self.normalize_email(email),
            password=password,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**kwargs):
        user = self.create_user(email=self.normalize_email(email),
            password=password,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True,default=uuid4)
    email = models.EmailField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

