from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, full_name, username, company_name, password=None):
        if not email:
            raise ValueError("User must have an email")

        if not username:
            raise ValueError("User must have a username")
        

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            full_name = full_name,
            company_name = company_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, email, full_name, username, company_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            full_name = full_name,
            company_name = company_name,
        )

        user.is_manager = True
        user.is_staff = True
        user.is_superuser =True

        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, full_name, username, company_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            full_name=full_name,
            company_name = company_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser =True

        user.save(using=self._db)
        
        return user



class Account(AbstractBaseUser):
    company_name    = models.CharField(max_length=100)
    full_name       = models.CharField(max_length=100)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)

    is_manager      = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'company_name']


    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


        