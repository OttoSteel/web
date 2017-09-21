from django.shortcuts import render
from django.http import HttpResponse, Http404
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from qa.models import QuestionManager

# Create your views here.

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    pageLimit = 10
    # Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
    qwests = Question.objects.all().order_by('-id')

    from django.core.paginator import Paginator

    page = request.GET.get('page') or 1
    try:
        page = int(page)
    except ValueError:
        page = 1
    paginator = Paginator(qwests, pageLimit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'questionList.html', {
        'title': 'qwests and answers',
        'list': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    pageLimit = 10
    # Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
    qwests = Question.objects.all().order_by('-likes')

    from django.core.paginator import Paginator

    page = request.GET.get('page') or 1
    try:
        page = int(page)
    except ValueError:
        page = 1
    paginator = Paginator(qwests, pageLimit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'questionList.html', {
        'title': 'popular quests',
        'list': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, quest_id):
    try:
        quest = Question.objects.get(id=quest_id)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.all().filter(question=quest)

    title = 'qwest ' + quest_id

    user = request.user

    #if user.is_authenticated():
        #form = AnswerForm(initial={'question': quest_id})

    return render(request, 'question.html', {
        'title': title,
        'question': quest,
        'list': answers,
        'form': form,
    })
