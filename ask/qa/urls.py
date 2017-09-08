from django.conf.urls import include, url

urlpatterns = [
        url(r'^$', qa.views.test, name='index'),
        url(r'^login/', qa.views.test, name='login'),
        url(r'^signup/', qa.views.test, name='signup'),
        url(r'^question/(?P<quest_id>[0-9]+)/$', qa.views.test, name='question'),
        url(r'^ask/', qa.views.test, name='ask'),
        url(r'^popular/', qa.views.test, name='popular'),
        url(r'^new/', qa.views.test, name='new'),
]

