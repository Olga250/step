from django.shortcuts import render
from django.http import HttpResponse  
# Create your views here.  
def test(request, *args, **kwargs):  
#   return HttpResponse('OK')  
def main(request):
    return HttpResponse('OK')
def draw_question(request, q_id):
    try:
        question = Question.objects.get(id = q_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'ask/question.html', {
       'question' : question,
       'title' : question.title,
       'text' : question.text, 
       })
return render(request, 'question_load.html', {
      'questions': page.object_list,
      'paginator': paginator, 'page': page,
    })
last_questions = Question.odjects.all()
last_questions = last_questions.order_by('-id')

