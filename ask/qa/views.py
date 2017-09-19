from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Question, Answer
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from models import QuestionManager

# Create your views here.

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request) :
	pageLimit = 10
	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
	quests = Question.objects.all().new()
	
	
	page = request.GET.get('page') or 1
	try :
		page = int(page)
	except ValueError :
		page = 1
	paginator = Paginator(quests, pageLimit)
	paginator.baseurl = '/?page='
	try :
		page = paginator.page(page)
	except EmptyPage :
		page = paginator.page(paginator.num_pages)
	return render(request, 'questionList.html', {
		'title' : 'quests and answers',
		'list' : page.object_list,
		'paginator' : paginator, 
		'page' : page,
    })
