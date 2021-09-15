from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def home(request):
     return redirect('/random_word')

def random_word(request):
     if 'attemps' not in request.session:
          request.session['attemps'] = 1
          attemps = request.session['attemps']
     else:
          attemps = request.session['attemps']
          attemps += 1
          request.session['attemps'] = attemps

     context = {
          'attemps' : attemps,
          'word' : get_random_string(length=14)
     }
     return render(request, 'random_word/home.html', context)
     return HttpResponse('llegue')

def reset(request):
     request.session.flush()
     return redirect('/random_word')
 