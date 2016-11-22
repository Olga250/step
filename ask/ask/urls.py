from django.conf.urls import include, url, patterns  
from django.contrib import admin 
admin.autodiscover() 
urlpatterns = patterns('', 
        url(r'^admin/', include(admin.site.urls)), 
	url(r'^$', 'qa.views.index', name='home'), 
 	url(r'^login/.*$', 'qa.views.test', name='login'), 
 	url(r'^signup/.*$', 'qa.views.test', name='signup'), 
 	url(r'^question/(?P<id>\d+)/', 'qa.views.question', name='question'), 
 	url(r'^ask/.*$', 'qa.views.test', name='ask'), 
 	url(r'^popular/', 'qa.views.popular', name='popular'), 
 	url(r'^new/.*$', 'qa.views.test', name='new')	 
 ) 


