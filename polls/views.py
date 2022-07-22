from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Question


# Create your views here.
def index(request):
    lst_latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'lst_latest_questions': lst_latest_questions
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    # the above is equivalent to:
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = f'Looking at results of question {question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f'Voting on question {question_id}')
