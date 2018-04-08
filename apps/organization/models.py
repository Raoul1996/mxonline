from datetime import datetime
from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="city_name")
    desc = models.CharField(max_length=200, verbose_name="city_desc")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "city"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="org_name")
    desc = models.TextField(verbose_name="org_desc")
    click_num = models.IntegerField(default=0, verbose_name="click_number")
    fav_num = models.IntegerField(default=0, verbose_name="favorite_number")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="cover_picture", max_length=100)
    address = models.CharField(max_length=150, verbose_name="org_address")
    city = models.ForeignKey(CityDict, verbose_name="city", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "course_org"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="teacher_name")
    work_years = models.IntegerField(default=0, verbose_name="work_year")
    work_company = models.CharField(max_length=50, verbose_name="work_company")
    work_position = models.CharField(max_length=50, verbose_name="work_position")
    point = models.CharField(max_length=50, verbose_name="point")
    click_num = models.IntegerField(default=0, verbose_name="click_number")
    fav_num = models.IntegerField(default=0, verbose_name="favorite_number")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = verbose_name
