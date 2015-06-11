from django.shortcuts import render
from django.http import HttpResponse  
from django.shortcuts import render_to_response  
from django.template import RequestContext, loader  

# Create your views here.
    #return HttpResponse("Hello, world. You're at the poll index.")    
def index(request):  
# View code here...  
    t = loader.get_template('index.html')  
    c = RequestContext(request, {'foo': 'bar'})  
    #return HttpResponse(t.render(c), content_type="application/xhtml+xml")
    return HttpResponse(t.render(c))
    #return render_to_response('index.html')

def aboutus(request):  
# View code here...  
    t = loader.get_template('about.html')  
    c = RequestContext(request, {'foo': 'bar'})  
    #return HttpResponse(t.render(c), content_type="application/xhtml+xml")
    return HttpResponse(t.render(c))
    #return render_to_response('index.html')