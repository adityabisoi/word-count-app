# from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html')

def count(request):
    sentence = request.GET['sentence']
    wordlist = sentence.split()
    length = len(wordlist)
    return render(request, 'count.html', {'length':length})