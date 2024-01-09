from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount', 'off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalize == "on":
        analyzed =""
        
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose': 'Capitalize', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            
        params = {'purpose': 'new line removed', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if spaceremover == "on":
        analyzed = ""

        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if (removepunc !="on" and capitalize !="on" and newlineremover !="on" and spaceremover !="on"):
        return HttpResponse("please select any one option..")
    
    return render(request, 'about.html', params)
