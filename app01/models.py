from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
# Create your models here.
from config import settings

User = settings.AUTH_USER_MODEL


class Memo(models.Model):
    title = models.CharField(null=False, max_length=50)
    memo = models.TextField(null=False, max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Manager(UserManager):

    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField('username', unique=True, max_length=50, blank=False)
    email = models.EmailField('email address', unique=True, blank=False)

    objects = Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



