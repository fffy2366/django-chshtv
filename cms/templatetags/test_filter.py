#coding:utf-8
#
#[django 自定义标签和过滤器](http://xiao80xiao.iteye.com/blog/519394)
#[Django 中 如何使用 settings.py 中的常量](http://www.yihaomen.com/article/python/407.htm)
#[](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/)

from django import template

register = template.Library()

def percent_decimal(value):
   
    value = float(str(value))
    value = round(value, 3)
    value = value * 100
   
    return str(value) + '%'

from django import template

register = template.Library()

register.filter('percent_decimal', percent_decimal) 