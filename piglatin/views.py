from django.http import HttpResponse
from django.shortcuts import render

def is_vowel(letter):
    letter = str.lower(letter)
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def home(request):
    return render(request, 'home.html')

def translate(request):
    words = request.GET['input_text'].split()
    ret = ""
    for word in words:
        if is_vowel(word[0]):
            ret += " " + word + "ay"
        else:
            ret += " " + word[1:] + word[0] + "ay"
    ret = str.strip(ret)
    return render(request, 'translate.html', {'original':" ".join(words), 'translation':ret})

def about(request):
    return render(request, 'about.html')