import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Words
from django.http import HttpResponseRedirect
from .forms import EventForm
from random import randint
# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')



@csrf_exempt
def add_word(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_word?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_word.html', {'form': form, 'submitted': submitted})



@csrf_exempt
def Show_all_words(request):
    words_list = Words.objects.filter(approved= True)
    count = Words.objects.all().count()
    return render(request,"all_words.html",{"words_list":words_list})



def Search_word(request):
    count = Words.objects.all().count()
    if request.method == "POST":
        search = request.POST.get("search") #Grab the search item
        word = Words.objects.filter(English_word__iexact =search, approved= True)
        if word.exists():
            return render(request,"search_page.html", {'search': search, 'word': word, "count":count})
        if not word:
            message = "המילה לא קיימת במאגר"
            return render(request,"search_page.html", {'message': message, "count":count})
    else:
        return render(request, "search_page.html", {"count": count})



# def practice(request):
#     words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
#     random_word_to_guess = random.choice(words_list) # Take one random words from the DB
#     word_1 = random.choice(words_list)
#     word_2 = random.choice(words_list)
#     word_3 = random.choice(words_list)
#     if request.method == "POST":
#         if request.GET.get('correct') == "correct": # if the user click on button that his name =correct - the choice is correct
#             message = "Correct answer"
#             return render(request, "practice.html", {'message': message})
#         else: # if the user click on other button that his name = incorrect - the choice is wrong and show him the massage
#             message = "wrong answer"
#             return render(request, "practice.html", {'message': message})
#
#     return render(request, "practice.html", {'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,})
#


def practice(request):
    words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
    random_word_to_guess = random.choice(words_list) # Take one random words from the DB
    word_1 = random.choice(words_list)
    word_2 = random.choice(words_list)
    word_3 = random.choice(words_list)
    if request.method == "POST":
        guess = request.GET.get("guess")
        if request.GET.get(guess) == 'correct': # if the user click on button that his name =correct - the choice is correct
            message = "Correct answer"
            return render(request, "practice.html", {'message': message,'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,})
        else: # if the user click on other button that his name = incorrect - the choice is wrong and show him the massage
            message = "wrong answer"
            return render(request, "practice.html", {'message': message,'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,})
    return render(request, "practice.html", {'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,})




