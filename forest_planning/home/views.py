from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'year': '202', 'list': [1,2,3]}
    return render(request, 'home.html', context)