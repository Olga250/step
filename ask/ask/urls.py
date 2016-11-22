from django.conf.urls import patterns, include, url
from django.contrib import admin
from qa.views import test, mainPage, popular, question
admin.autodiscover()
urlpatterns = patterns('',  
#    urlpatterns = [ 
     url(r'^$', mainPage, name = 'mainPage'), 
     url(r'^popular/$', popular, name = 'popular'), 
     url(r'^question/(?P<slug>\w+)/$', question, name='question'), 
     #url(r'^admin/', admin.site.urls), 
     #url(r'^login/', test, name = 'login'), 
     #url(r'^signup/', test, name = 'signup'), 
     #url(r'^ask/', test, name = 'ask'), 
     #url(r'^new/', test, name = 'new'), 
) 

  
