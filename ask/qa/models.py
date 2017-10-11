from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
        def new(self):
                return self.order_by('-id')

        def popular(self):
                return self.order_by('-rating')

class Question(models.Model) :
	#id = models.IntegerField(primary_key=True)
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name='+', default=1)
	likes = models.ManyToManyField(User, default=1)
	
	def get_absolute_url(self) :
		return '/question/%d/' % self.pk

class Answer(models.Model) :
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
        author = models.ForeignKey(User, related_name='+', default=1)

