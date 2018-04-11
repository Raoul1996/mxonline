# _*_ coding: utf-8 _*_
__date__ = '2018/4/11 下午10:45'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDitAdmin(object):
    list_field = ['name', 'desc', 'add_time']
    search_field = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_field = ['name', 'desc', 'image', 'address', 'city', 'add_time']
    search_field = ['name', 'desc', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_field = ['org', 'name', 'work_years', 'work_company', 'point', 'add_time']
    search_field = ['org', 'name', 'work_years', 'work_company', 'point']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'point', 'add_time']


xadmin.site.register(CityDict, CityDitAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
