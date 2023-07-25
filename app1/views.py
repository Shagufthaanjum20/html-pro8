from django.shortcuts import render

# Create your views here.
def html(request):
    return render(request,'new.html')
    
def html_response(request):
    return render(request,'index.html')   
