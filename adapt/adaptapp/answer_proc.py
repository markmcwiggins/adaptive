#!/usr/bin/python
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template


def answer_proc(request):
    return HttpResponseRedirect('/wrong')
