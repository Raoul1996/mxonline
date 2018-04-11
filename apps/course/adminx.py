# _*_ coding: utf-8 _*_
__date__ = '2018/4/11 下午10:17'
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'student', 'fav_num', 'image', 'click_num',
                    'add_time']
    search_field = ['name', 'desc', 'detail', 'degree', 'student']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_field = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_field = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_field = ['course', 'name', 'download' 'add_time']
    search_field = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
