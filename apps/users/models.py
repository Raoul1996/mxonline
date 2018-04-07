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


class EmailVerifyRecord(models.Model):
    SEND_TYPE = (('register', u'注册'), ('forget', u'找回密码'))
    code = models.CharField(max_length=20, verbose_name=u"verify_code")
    email = models.EmailField(max_length=50, verbose_name=u"email")
    send_type = models.CharField(choices=SEND_TYPE, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = u"email_verify_code"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"banner", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"access_address")
    index = models.IntegerField(default=100, verbose_name=u"order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = u"banner"
        verbose_name_plural = verbose_name
