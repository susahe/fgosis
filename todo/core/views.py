from django.shortcuts import render

# Create your views here.
from models import todo,project,maintask,subtask
from django.shortcuts import render_to_response

def index(request):
	
	return render_to_response('index.html',)


