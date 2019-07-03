from django.shortcuts import render
from django.http import HttpResponse


def resume_index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "resume_index.html")