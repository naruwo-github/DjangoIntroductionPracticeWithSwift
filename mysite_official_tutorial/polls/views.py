from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.http import Http404
# Create your views here.

"""
各ビューは2つの役割を持つ
・リクエストされたページのコンテンツを含むHttpResponseオブジェクトを返す
・Http404のような例外の検出
それ以外の処理はユーザ次第！
pythonライブラリを使って、なんでも実現できる！
"""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # request.POSTは、辞書ライクなオブジェクト
    # request.POST['choice']は、選択された選択肢のIDを文字列として返す
    # request.POSTの値は常に文字列
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  # Postデータにchoiceがなければ、request.POSTがKeyErrorを送出
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータが成功した場合はHttpResponseRedirectを常に返すべき
        # reverse()関数を使うと、ビュー関数中でのURLのハードコードを防げる
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
