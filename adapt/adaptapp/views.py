from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.core.context_processors import csrf
import random
import os
import glob

# Create your views here.

def gm(request):  # get message
    storage =  messages.get_messages(request)
    m = ''
    for m in storage:
        print m
    return m

def index(request):
    return HttpResponse('hello, main menu!')

def wrong(request):
    m = gm(request)
    return doit(request,'wrong.html',m)
    #return HttpResponse('wrong answer!')

def right(request):
    m = gm(request)
    return doit(request, 'right.html',m)
#    return HttpResponse('yep, you got it!')

def randpage(request):
    tees = glob.glob('adaptapp/templates/[0-9][0-9][0-9].html')
    print tees
    print os.getcwd()
    nh = random.randint(0,len(tees) - 1)
    tee = tees[nh]
    (ig,ig2,h) = tee.split('/')
    return HttpResponseRedirect('/adaptapp/%s' % h)
    

def answer_proc(request):
    c = {}
    c.update(csrf(request))
    ra = request.POST['ra']
    (n,s) = ra.split(',')
    suitans = request.POST['suit']
    nans = request.POST['amp'] # 'amplitude
    if request.POST.get('explanation'):
        messages.success(request,request.POST['explanation'])
    if (n == nans and s == suitans):
        return HttpResponseRedirect('/adaptapp/right',c)
    else:
        return HttpResponseRedirect('/adaptapp/wrong',c)

def doit(request,h,msg=''):
    c = { }
    c.update(csrf(request))
    c['exp'] = msg
    return render_to_response(h,c)

def hand(request):
    path = request.get_full_path()
    (ig,nore,html) = path.split('/')
    return doit(request, html)

def twod(request):
    return doit(request,'2d.html')

def twoclubs(request):
    return doit(request,'2clubs.html')

def oneheart(request):
    return doit(request,'1heart.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticat(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin.html')
    else:
        return HttpResponseRedirect('/accounts/invalid.html')


        
