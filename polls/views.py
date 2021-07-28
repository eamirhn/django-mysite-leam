
from .models import information, storyData
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import addStoryForm
from django.views import generic



#  In Django, web pages and other content are delivered by views.
#  Each view is represented by a Python function (or method, in the case of class-based views)

def index(request):
    data='<h3>This is a Heading</h3>'
    return HttpResponse(data)

# Create your Form
def text(request): 
    if request.method == "POST":
        form=addStoryForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            image = form.cleaned_data['image']
            author=request.user
            
            blog=storyData.objects.create(title=title,story=content,author=author,image=image)
            blog.save()
           
            return HttpResponse('Created!')
    else:
        form=addStoryForm()
    arg={'form':form}
    return render(request,'polls/blog_page.html',arg)     
    



def detail(request,question_id):
    return HttpResponse(f'this is your questin {question_id}')
def result(request , question_id):
    return HttpResponse(f'this is the result {question_id}')

def vote(request, var):
    context={'var':var}
    return render(request,'polls/vote.html',context)

def homePage(request):
    inform = information.objects.all()
    arg={'inform':inform}
    return render(request , 'polls/home.html',arg)

# Generic view : build in function to make it simple and easier
# in order to use GV you need to use class which heritate form django.views.generic.
# and in url you have to use ClassName.as_view()
 
class storyListsGeneric(generic.ListView):
    template_name='polls/listsofstories.html'
    context_object_name='lists'

    def get_queryset(self):
        return storyData.objects.all() 



# def storyLists(request):
#     data = storyData.objects.all()
#     arg = {'lists':data}
#     return render(request,'listsofstories.html',arg)


# def storyteller(request,storyid):
#     data = storyData.objects.get(id=storyid) # get info from model
#     arg={'story':data}
#     return render(request,'story.html',arg )

class storyTellerGeneric(generic.DetailView):
    template_name = 'polls/story.html'
    model = storyData # django make all letters lower , use this in tamplate tags
    



def storyLike(request,id):
    story = storyData.objects.get(id=id)
    user = request.user
    if user.is_authenticated:

        if user in story.likes.all():
            return HttpResponse('you have already liked this story')
        else:
            story.likes.add(user)
            return redirect('polls:story_datail',id)
    else:
        return HttpResponse('you are not allow to like this story')


def storyUnlike(request,id):
    story = storyData.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        if user in story.likes.all():
            story.likes.remove(user)
            return redirect('polls:story_datail',id)
        else:
            return HttpResponse('you have never liked this')
    else:
        return HttpResponse('you are not allow to like this')
