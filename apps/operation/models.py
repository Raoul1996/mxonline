from datetime import datetime

from django.db import models

from users.models import UserProfile
from course.models import Course


# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    mobile = models.CharField(max_length=11, verbose_name="mobile")
    course = models.CharField(max_length=50, verbose_name="course_name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "ask"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="course", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "course"
        verbose_name_plural = verbose_name


class UserComments(UserCourse):
    """
    课程评论
    """
    comments = models.CharField(max_length=200, verbose_name="comment")

    class Meta:
        verbose_name = "comments"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    TYPE = ((1, "Course"), (2, "Organization"), (3, "Teacher"))
    user = models.ForeignKey(UserProfile, verbose_name="user", on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name="data_id")
    fav_type = models.IntegerField(choices=TYPE, default=1, verbose_name="favorite_type")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "favorite"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="receive_user")
    message = models.CharField(max_length=500, verbose_name="msg_content")
    has_read = models.BooleanField(default=False, verbose_name="has_read_msg")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "message"
        verbose_name_plural = verbose_name
