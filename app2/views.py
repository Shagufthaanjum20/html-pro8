from django.shortcuts import render

# Create your views here.
def new1(request):
    return render(request,('new1.html'))
   

def new2(request):
    return render(request,('new2.html'))