# _*_ coding: utf-8 _*_
__date__ = '2018/4/11 下午10:44'

import xadmin

from .models import UserAsk, UserCourse, UserComments, UserFavorite, UserMessage


class UserAskAdmin(object):
    list_field = ['name', 'mobile', 'course', 'add_time']
    search_field = ['name', 'mobile', 'course']
    list_filter = ['name', 'mobile', 'course', 'add_time']


class UserCourseAdmin(object):
    list_field = ['user', 'course', 'add_time']
    search_field = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserCommentsAdmin(object):
    list_field = ['user', 'course', 'comments', 'add_time']
    search_field = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_field = ['user', 'fav_id', 'fav_type', 'add_time']
    search_field = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_field = ['user', 'message', 'has_read', 'add_time']
    search_field = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserComments, UserCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
