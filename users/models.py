from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.
class CustomAccountManager(BaseUserManager):
	def create_user(self, email, password):
		user = self.model(email=email, password=password)
		user.set_password(password)
		user.is_staff = False
		user.is_active = True
		user.is_superuser = False
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.model(email=email, password=password)
		user.is_active = True
		user.is_staff = True
		user.is_superuser = True
		user.set_password(password)
		user.save(using=self._db)

	def get_by_natural_key(self, email_):
		print(email_)
		return self.get(email=email_)


class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=50, blank=True, null=True, default=None)
	last_name = models.CharField(max_length=50, blank=True, null=True, default=None)
	facebook_id = models.CharField(max_length=200, unique=True, blank=True, null=True, default=None)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	USERNAME_FIELD = 'email'

	objects = CustomAccountManager()

	def get_short_name(self):
		return self.email

	def natural_key(self):
		return self.email

	def __str__(self):
		return str(self.email)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	Token.objects.get_or_create(user=instance)