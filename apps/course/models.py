# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models


# Create your models here.

class Course(models.Model):
    DEGREE = (("junior", "初级"), ("intermediate", "中级"), ("senior", "高级"))
    name = models.CharField(max_length=50, verbose_name=u"course_name")
    desc = models.CharField(max_length=300, verbose_name=u"course_description")
    detail = models.TextField(verbose_name="course_detail")
    degree = models.CharField(choices=DEGREE, max_length=15)
    learn_time = models.IntegerField(default=0, verbose_name="learn_time(minute)")
    student = models.IntegerField(default=0, verbose_name="student_number")
    fav_num = models.IntegerField(default=0, verbose_name="favorite")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="cover_picture", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name="click_number")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "course"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="course", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="lesson_name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Course, verbose_name="lesson", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="video_name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="course", on_delete=models.CASCADE)
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="resource_file", max_length=100)
    name = models.CharField(max_length=100, verbose_name="resource_name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "resource"
        verbose_name_plural = verbose_name
