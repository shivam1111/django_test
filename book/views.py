from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def search_form(request):
#     return render_to_response('search_form.html',{})
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = "The string searched was %s"%(request.GET['q'])
    else:
        message = "NO search String"
    return HttpResponse(message)