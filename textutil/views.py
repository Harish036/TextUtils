from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc' , 'off')
    capvar = request.POST.get('capitalize', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspace = request.POST.get('extraspaceremover', 'off')
    newline = request.POST.get('newlineremove', 'off')
    analyzed = ""
    if removepunc == 'on':
        punctuations = '''!(){}[];:,<.>/?@#$%^&*'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = { 'purpose' : 'Removed Punctuation', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html', params)
    if capvar == 'on':
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized string', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if charcount == 'on':
        charnumber = 0
        for char in djtext:
            charnumber += 1
        params = {'purpose': 'Counting the characters', 'analyzed_text': charnumber}
        return render(request, 'analyze.html', params)
    if extraspace == 'on':
        for ndex, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + djtext[index]
        params = {'purpose': 'Removing the extra spaces from the line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if newline == 'on':
        for char in djtext:
            if char == '\n' or char == '\r':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removing newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    return HttpResponse("Error!")