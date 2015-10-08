#-*-coding:utf-8-*- 
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from cms import backend
from django.conf import settings  
from django.conf.urls.static import static 

#[Django的url用法](http://blog.csdn.net/FeeLang/article/details/25245935)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chshtvp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #backend
    url(r'^backstage/', include('cms.urls')),
    #home
    url(r'^$', 'cms.views.index', name='index'),
    url(r'^aboutus$', 'cms.views.aboutus', name='aboutus'),
    url(r'^captcha/', include('captcha.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'backstage/login.html'}),
) + static(settings.STATIC_URL)

urlpatterns += patterns('lession.views', 
    (r'^book/(?p<year>\d))
)