from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question;

# Create your views here.
def index(req):
    latest_ques_list =  Question.objects.order_by('-pub_date')[:5]
    print(latest_ques_list)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_ques_list' : latest_ques_list
    }
    return HttpResponse(template.render(context, req))

def detail(req, question_id):
    print('Inside of details.....')
    try:
        question = Question.objects.get(pk = question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    # question = get_object_or_404(Question, pk=question_id)    
    return HttpResponse(req, 'polls/detail.html', {'question': question})

def result(req, question_id):
    resp = "Youre loooking at  result of question %s."
    return HttpResponse(resp % question_id)

def vote(req, question_id):
    return HttpResponse("You are voting on question %s." % question_id)