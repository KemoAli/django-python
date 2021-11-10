from django.shortcuts import render
from django.http import HttpResponse, response;

# Create your views here.
def index(req):
    return HttpResponse("Hello world!")

def detail(req, question_id):
    return HttpResponse('You are looking at question %s.' % question_id)

def result(req, question_id):
    resp = "Youre loooking at  result of question %s."
    return HttpResponse(resp % question_id)

def vote(req, question_id):
    return HttpResponse("You are voting on question %s." % question_id)