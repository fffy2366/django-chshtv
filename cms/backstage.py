#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse  
from django.shortcuts import render_to_response  
from django.template import RequestContext, loader  
from form import CaptchaTestForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json

from django.contrib.auth.decorators import login_required

# Create your views here.
    #return HttpResponse("Hello, world. You're at the poll index.")    
@login_required
def index(request):  
# View code here...  
    t = loader.get_template('backstage/index.html')  
    c = RequestContext(request, {'foo': 'bar'})  
    #return HttpResponse(t.render(c), content_type="application/xhtml+xml")
    return HttpResponse(t.render(c))
    #return render_to_response('index.html')

#[Django框架学习-Templates进阶用法--上]（http://www.cnblogs.com/btchenguang/archive/2012/09/01/2666763.html)
def login(request):  
    #刷新验证码
    if request.GET.get('newsn')=='1':
        csn=CaptchaStore.generate_key()
        cimageurl= captcha_image_url(csn)
        return HttpResponse(cimageurl)

    t = loader.get_template('backstage/login.html')  
    c = RequestContext(request, {'foo': 'bar'})

    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True

        to_json_response = dict()
        to_json_response['status'] = 0
        to_json_response['form_errors'] = form.errors

        to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
        to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

        return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    else:
        form = CaptchaTestForm()  

        #return HttpResponse(t.render(c))
        #return render_to_response('backend/login.html',locals())
        return render_to_response('backstage/login.html',
            locals(),
            context_instance=RequestContext(request, processors=[]))
