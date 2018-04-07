# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    GENDER = (("male", u"男"), ("female", u"女"))
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="", )
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True, )
    gender = models.CharField(max_length=5, choices=GENDER, default="female", )
    address = models.CharField(max_length=100, default="", )
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True, )
    avatar = models.ImageField(max_length=100, upload_to="avatar/%Y/%m", default=u"avatar/default.png", )

    class Meta:
        verbose_name = u"用户信息",
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
