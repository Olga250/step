from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
#class QuestionManager(models.Manager):                                          
  #     def new():                                                              
   #             pass                                                            
    #    def popular():                                                          
     #         pass
class Question(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User)
 
#class Question(models.Model):                                                   
 #   objects = QuestionManager() 
  #  title = models.CharField(max_length=255)  
   # text = models.TextField()  
  #  rating = models.IntegerField(default=0)  
 #   added_at = models.DateTimeField(auto_now=True)  
#    author = models.ForeignKey(User, related_name="question_author")  
    likes = models.ManyToManyField(User)  
def get_absolute_url(self):
   return reverse('question', kwargs={"id": self.id})
def __unicode__(self):
    return self.title
class Answer(models.Model):  
    text = models.TextField()  
    added_at = models.DateTimeField(auto_now=True)  
    question = models.ForeignKey(Question)  
    author = models.ForeignKey(User, related_name="answer_author")  
