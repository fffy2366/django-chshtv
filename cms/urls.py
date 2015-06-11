from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static 
from cms.forms import AjaxExampleForm
from cms.forms import CommentCreateView


urlpatterns = patterns('',
    #backend
    url(r'^$', 'cms.backstage.index', name='index'),
    url(r'^login$', 'cms.backstage.login', name='login'),
    url(r'^loginact$', AjaxExampleForm.as_view(), name='ajax_example_form'),
    url(r'^comment_create$', CommentCreateView.as_view()),
) + static(settings.STATIC_URL)
