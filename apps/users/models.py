# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    GENDER = (("male", "male"), ("female", "female"))
    nick_name = models.CharField(max_length=50, verbose_name="nickname", default="", )
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True, )
    gender = models.CharField(max_length=10, choices=GENDER, default="female", )
    address = models.CharField(max_length=100, default="", )
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True, )
    avatar = models.ImageField(max_length=100, upload_to="avatar/%Y/%m", default="avatar/default.png", )
    # class Meta:
    #     verbose_name = 'UserProfile',
    #     verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    SEND_TYPE = (('register', 'register'), ('forget', 'found password'))
    code = models.CharField(max_length=20, verbose_name="verify_code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(choices=SEND_TYPE, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "email_verify_code"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="banner", max_length=100)
    url = models.URLField(max_length=200, verbose_name="access_address")
    index = models.IntegerField(default=100, verbose_name="order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = verbose_name
