#!/usr/bin/env python
#coding:utf-8
#
#[django 自定义标签和过滤器](http://xiao80xiao.iteye.com/blog/519394)
#[Django 中 如何使用 settings.py 中的常量](http://www.yihaomen.com/article/python/407.htm)

from django import template
from django.conf import settings  

register = template.Library()

class TestNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return "xxxxx"

def test(parser, token):
    return TestNode()



register.tag('my_tag', test)

