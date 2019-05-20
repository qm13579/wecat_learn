from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        # user.is_superuser = True
        user.is_admin=True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=64, verbose_name="姓名")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    # host_to_remote_user=models.ManyToManyField('HostToRemoteUser')
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    def has_perm(self, perm ,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    def __str__(self):              # __unicode__ on Python 2
        return self.email
    class Meta:
        permissions=()

class Test(models.Model):
    uasername = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    age = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True,)
class Session(models.Model):
    session_key = models.CharField(max_length=246)
    session_value = models.CharField(max_length=246)
    session_date =  models.DateTimeField(auto_now_add=True)
    userprofile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)

    def __str__(self):
        return self.session_key