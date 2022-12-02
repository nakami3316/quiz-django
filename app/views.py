from django.shortcuts import render
from .models import Quiz
# #下記はtodoを参考にした
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
#下記のコードは追加
def templates(request):
    question = Quiz.objects.order_by('?').first()
    context = {'question': question}
    return render(request,'templates.html',context)

def move_to_seikaipage(request):
    return render(request, 'seikaipage.html')

def move_to_fuseikaipage(request):
    return render(request, 'fuseikaipage.html')

def quiz_complete(request):
    return render(request, 'quiz_complete.html')

def LoginView(request):
    return HttpResponseRedirect('social:begin', kwargs=dict(backend='google-oauth2'))

def index(request):
    return render(request,'templates.html')

class TodoCreate(CreateView):
    model = Quiz
    fields = "__all__"
    success_url = reverse_lazy('complete')
