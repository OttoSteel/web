from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.test, name='login'),
    url(r'^signup/', views.test, name='signup'),
    url(r'^question/(?P<quest_id>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^answer/', views.answer, name='answer'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.test, name='new'),
]
