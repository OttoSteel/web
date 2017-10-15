from django.shortcuts import render
from django.http import HttpResponse, Http404
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from qa.models import QuestionManager
from qa.forms import AskForm, AnswerForm

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    pageLimit = 10
    # Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
    qwests = Question.objects.new()

    page = request.GET.get('page', 1)
    
    paginator = Paginator(qwests, pageLimit)
    paginator.baseurl = 'question/'
    page = paginator.page(page)
  
    return render(request, 'questionList.html', {
        'title': 'qwests and answers',
        'list': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    pageLimit = 10
    # Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
    qwests = Question.objects.popular()

    page = request.GET.get('page', 1)
    
    paginator = Paginator(qwests, pageLimit)
    paginator.baseurl = 'question/'
    
    page = paginator.page(page)
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

    title = 'qwest_' + quest_id

    #user = request.user

    #if user.is_authenticated():
        #form = AnswerForm(initial={'question': quest_id})

    return render(request, 'question.html', {
        'title': title,
        'question': quest,
        'list': answers,
        #'form': form,
    })

def ask(request) :
	user = request.user
	if request.method == "POST" :
		#print("POST!!!!!!!!!!!!!!!!!!!!!!!!!")
		form = AskForm(request.POST)
		if form.is_valid() :
			
			quest = form.save()
				#print("QUEST IS CREATE!!!!!!!!!!")
			url = quest.get_absolute_url()
				#print("URL = " + url +"!!!!!!!!!")
			return HttpResponseRedirect(url)
			
	else :
		form = AskForm()
	return render(request, 'ask_add.html', {
		'form' : form
	})
	
def answer(request) :
	user = request.user
	if request.method == "POST" :
		form = AnswerForm(request.POST)
		if form.is_valid():
			
			answer = form.save()
			url = '/question/' + form.question
			return HttpResponseRedirect(url)
	
