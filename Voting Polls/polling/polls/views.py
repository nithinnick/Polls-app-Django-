from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


# Create your views here.
# to get all the questions
def index(request):
    ques = Question.objects.all()
    return render(request, 'index.html', {'ques': ques})


# to show specific question and choices
def details(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'details.html', {'question': question})


# Get question and display result
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # questi = Question.objects.get(pk=question_id)
    # choic = Choice.objects.get(pk=question_id)
    return render(request, 'results.html', {'choice': question})


# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
