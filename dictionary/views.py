from django.shortcuts import render, redirect
from PyDictionary import PyDictionary

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(request):
    # Get request is getting the name attribute of the form input
    term = request.GET.get('search')
    antonyms = None
    if not term:
        return redirect('/')
    else:
        dictionary = PyDictionary()
        definitions = dictionary.meaning(term)
        synonyms = dictionary.synonym(term)
        antonyms = dictionary.antonym(term)
        context = {
            'term': term,
            'definitions': definitions,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
        return render(request, 'word.html', context)