from django.shortcuts import render_to_response
from blog.models import posts

# Create your views here.
def home(request):
    return render_to_response('index.html')

