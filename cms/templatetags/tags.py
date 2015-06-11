#!/usr/bin/env python
#coding:utf-8
#
#[django 自定义标签和过滤器](http://xiao80xiao.iteye.com/blog/519394)
#[Django 中 如何使用 settings.py 中的常量](http://www.yihaomen.com/article/python/407.htm)

from django import template
from django.conf import settings 

register = template.Library()


# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
