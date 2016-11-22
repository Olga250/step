 from django.shortcuts import render 
 # Create your views here. 
 from django.http import HttpResponse, HttpResponseBadRequest 
 from django.http import Http404 
 from django.shortcuts import get_object_or_404 
 from models import Question, Answer 
 from django.core.paginator import Paginator, EmptyPage 
 from django.core.urlresolvers import reverse 
def test(request, *args, **kwargs): 
     return HttpResponse('test') 
 def index(request) : 
 	pageLimit = 10 
 	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc() 
        qwests = Question.objects.all().order_by('-id') 
 	from django.core.paginator import Paginator 
	page = request.GET.get('page') or 1 
 	try : 
 		page = int(page) 
 	except ValueError : 
 		page = 1 
 	paginator = Paginator(qwests, pageLimit) 
 	paginator.baseurl = '/?page=' 
 	try : 
 		page = paginator.page(page) 
 	except EmptyPage : 
 		page = paginator.page(paginator.num_pages) 
 	return render(request, 'questionList.html', { 
 		'title' : 'qwests and answers', 
 		'list' : page.object_list, 
 		'paginator' : paginator, 
 		'page' : page, 
 	}) 
 def popular(request) : 
 	pageLimit = 10 
 	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc() 
 	qwests = Question.objects.all().order_by('-likes') 
	from django.core.paginator import Paginator 
	page = request.GET.get('page') or 1 
 	try : 
 		page = int(page) 
 	except ValueError : 
 		page = 1 
 	paginator = Paginator(qwests, pageLimit) 
 	paginator.baseurl = '/?page=' 
 	try : 
 		page = paginator.page(page) 
 	except EmptyPage : 
 		page = paginator.page(paginator.num_pages) 
 	return render(request, 'questionList.html', { 
 		'title' : 'popular quests', 
 		'list' : page.object_list, 
 		'paginator' : paginator, 
 		'page' : page, 
 	}) 
 def question(request, id): 
 question = get_object_or_404(Question, pk=id) 
 answers = Answer.objects.filter(question = question) 
 return render(request, 'question.html', { 'user':request.user, 'question':question, 'answers':answers, }) 

 


