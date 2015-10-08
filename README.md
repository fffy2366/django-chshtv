##install

##创建工程
1.生成
```
django-admin.py startproject chshtvp
cd chshtvp/
python manage.py startapp cms
```
2.settting.py，将demoapp加入到INSTALLED_APPS
```
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
)
```
3.修改settting.py，将默认的sqlite数据库换成mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chshtvp',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',                  
    }
}

4.在demoproject下输入：python manage.py dbshell，如果能正常进入mysql命令行，则说明连接成功
5.启动应用

- 同步数据库：执行python manage.pysyncdb，第一次启动需要创建superuser，用来管理django后台
    ```
    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blak to use 'gouxulei'): frank
    Email address: fengxuting@gmail.com
    Password: 2****8
    Password (again):
    Superuser created successfully.
    ```
    
- 启动服务：python manage.py runserver

##template
1.
{% load staticfiles %}
{% static "img/menu2_bg03.png" %}

2.{{{{STATIC_URL}}img/kv_01.jpg 
[If {{ STATIC_URL }} isn’t working in your template, you’re probably not using RequestContext when rendering the template.](https://docs.djangoproject.com/en/1.4/howto/static-files/)

3.

##图片验证码
```
su
pip install django-simple-captcha
```

##Model 生成sql
python manage.py sqlall cms
CommandError: App 'cms' has migrations. Only the sqlmigrate and sqlflush commands can be used when an app has migrations.

python manage.py syncdb
python manage.py makemigrations
python manage.py migrate


python manage.py migrate cms
失败执行下面
python manage.py sqlmigrate cms 0002_auto_20151002_1430


python manage.py sqlmigrate cms 0001_initial


python manage.py syncdb
python manage.py sql appname

[Getting __init__() got an unexpected keyword argument 'instance' with CreateView of Django](http://stackoverflow.com/questions/16079299/getting-init-got-an-unexpected-keyword-argument-instance-with-createview)
[Advanced Django Class-based Views, ModelForms and Ajax Example Tutorial](http://chriskief.com/2013/10/29/advanced-django-class-based-views-modelforms-and-ajax-example-tutorial/)

[django中验证码——django-simple-captcha](http://blog.csdn.net/shanliangliuxing/article/details/9214181)
[官方文档](https://django-simple-captcha.readthedocs.org/en/latest/usage.html)

[CreateView](https://docs.djangoproject.com/en/1.7/ref/class-based-views/#django.views.generic.edit.CreateView)


[免费托管服务器](https://www.heroku.com/)

[使用Django1.7开发博客教程 - 目录汇总贴](http://my.oschina.net/yidao620c/blog/343174)
[Django 站点部署和管理常用命令](http://www.oschina.net/question/234345_54799)
[The Django Book](http://www.djangobook.com/en/2.0/index.html)
[Nginx+uWSGI 部署 Django 应用](http://www.oschina.net/question/54100_30386)
[django从数据库中生成model文件。（sql schemas -> model）](http://silo.blog.163.com/blog/static/21363515320115121500247/)

[设置 Sublime Text 的 Python 开发环境](http://www.open-open.com/lib/view/open1369960978459.html)

##ffmpeg
###安装
http://wiki.razuna.com/display/ecp/FFMpeg+Installation+on+CentOS+and+RedHat#FFMpegInstallationonCentOSandRedHat-InstallX264
###mp4 to flv
ffmpeg -i oceans.mp4 -ab 56 -ar 22050 -b 500 -r 15 -s 320x240 test.flv

###截图
ffmpeg -i oceans.mp4 -c:v libx264 -y -f image2 -ss 8 -t 0.001 -s 350x240 xxx.jpg

ffmpeg -i "test.flv" -y -f image2 -ss 8 -t 0.001 -s 350x240 'test.jpg'

