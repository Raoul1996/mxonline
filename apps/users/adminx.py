# _*_ coding: utf-8 _*_
__date__ = '2018/4/10 下午10:40'

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
