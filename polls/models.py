from django.db import models
import datetime
from django.db.models.fields import CharField, EmailField
from django.utils import timezone
from django.contrib.auth.models import User

#The name of each Field instance (Question , Choice) 
# You’ll use this value in your Python code, and your database will use it as the column name.

'''
each model is represented by a class that subclasses django.db.models.Model.
 Each model has a number of class variables, each of which represents a database field in the model.

Each field is represented by an instance of a Field class – e.g.,
 CharField for character fields and DateTimeField for datetimes.
  This tells Django what type of data each field holds.

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ForeignKey. That tells Django each Choice is related to a single Question. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class information(models.Model):
    name = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    adress = models.TextField()
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.name 



class storyData(models.Model):
    title = models.CharField(max_length=60)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)

    # ForeignKey is used for one to many relationship
    author = models.ForeignKey(User ,models.CASCADE,null=True,blank=True)
    # NULL AND BLANK IS FOR WHETER PREVIOS OBJECTS HAS AUTHOR ATRIBIUTE OR NOT .it's okay or not
    #CASCADE : When the referenced object is deleted, also delete the objects that have references


    image = models.ImageField(upload_to='%Y/%m/%d',null=True,blank=True) # this will save files into folders like (2021/05/19)
    # for many to many relationship
    # if there was two relationship in one model, you need to set a related-name
    likes = models.ManyToManyField(User,related_name='storyLike',blank=True) 


    def __str__(self):
        return self.title


    def getsnippet(self):
        return self.story[0:65] + ' .....'
    '''
1   Change your models (in models.py).
2   Run python manage.py makemigrations to create migrations for those changes
3   Run python manage.py migrate to apply those changes to the database. 
    '''