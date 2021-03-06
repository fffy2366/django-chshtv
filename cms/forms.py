#-*-coding:utf-8-*-
from django import forms
from captcha.fields import CaptchaField

from django.views.generic.edit import CreateView
from cms.mixins.ajaxformresponse import AjaxFormResponseMixin

from django.views.generic.edit import View
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json

from cms.models import Admin

from django.conf import settings
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()

class AjaxForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Admin

class AjaxExampleForm(AjaxFormResponseMixin,CreateView):
    template_name = ''
    form_class = AjaxForm

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    def form_valid(self, form):
        #form.save()
        if self.request.is_ajax():
            to_json_response = dict()

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            #[验证用户名密码](http://www.cnblogs.com/linjiqin/p/3638501.html)
            username = self.request.POST['username']
            password = self.request.POST['password']
            if username=="" or username.isspace():
                to_json_response['status'] = 0
                to_json_response['data'] = "用户名不能为空"
            if password=="" or password.isspace():
                to_json_response['status'] = 0
                to_json_response['data'] = "密码不能为空"

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(self.request, user)
                    to_json_response['status'] = 1
                    to_json_response['data'] = "OK"
                else:
                    to_json_response['status'] = 0
                    to_json_response['data'] = "["+username+"]已被暂时禁用"
            else:
                to_json_response['status'] = 0
                to_json_response['data'] = "用户名或密码不正确，请重试"

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')

class JSONMixin(object):
    def render_to_response(self, context, **httpresponse_kwargs):
        return self.get_json_response(
            self.convert_context_to_json(context),
            **httpresponse_kwargs
        )
    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(
            content,
            content_type='application/json',
            **httpresponse_kwargs
        )
    def convert_context_to_json(self, context):
        u""" This method serialises a Django form and
        returns JSON object with its fields and errors
        """
        form = context.get('form')
        to_json = {}
        options = context.get('options', {})
        to_json.update(options=options)
        to_json.update(success=context.get('success', False))
        fields = {}
        for field_name, field in form.fields.items():
            if isinstance(field, DateField) \
                    and isinstance(form[field_name].value(), datetime.date):
                fields[field_name] = \
                    unicode(form[field_name].value().strftime('%d.%m.%Y'))
            else:
                fields[field_name] = \
                    form[field_name].value() \
                    and unicode(form[field_name].value()) \
                    or form[field_name].value()
        to_json.update(fields=fields)
        if form.errors:
            errors = {
                'non_field_errors': form.non_field_errors(),
            }
            fields = {}
            for field_name, text in form.errors.items():
                fields[field_name] = text
            errors.update(fields=fields)
            to_json.update(errors=errors)
        return json.dumps(to_json)

class CommentCreateView(JSONMixin, CreateView):
    form_class = AjaxForm

