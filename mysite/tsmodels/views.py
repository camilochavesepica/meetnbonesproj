
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = ['Forecast', 'Forecast Components']
    template = loader.get_template('tsmodels/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def forecast(request):
    header = "You're looking at the Forecast "
    template = loader.get_template('tsmodels/forecast.html')
    context = {
        'header': header,
    }
    return HttpResponse(template.render(context, request))

def components(request):
    header = "You're looking at the Forecast Components"
    template = loader.get_template('tsmodels/components.html')
    context = {
        'header': header,
    }
    return HttpResponse(template.render(context, request))


def models(request, id):
    return HttpResponse("You're looking at model %s." % id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
