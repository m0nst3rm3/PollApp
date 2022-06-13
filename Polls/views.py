from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Questions, Choice
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'Polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')[:5]


class DetailView(generic.DetailView):
    model = Questions
    context_object_name = 'question'
    template_name = 'Polls/detail.html'

    def get_queryset(self):
        return Questions.objects.filter(published_on__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    context_object_name = 'question'
    template_name = 'Polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'Polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))


