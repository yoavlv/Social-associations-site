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
    words_list.order_by("-pub_date")
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




def practice(request):
    words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
    random_word_to_guess = random.choice(words_list) # Take one random words from the DB
    word_1 = random.choice(words_list)
    word_2 = random.choice(words_list)
    word_3 = random.choice(words_list)
    quiz_list = [word_1, word_2, word_3, random_word_to_guess]
    random_list = random.shuffle(quiz_list)
    count = 0
    correct_answer = 0
    incorrect_answer = 0
    n_list = ["correct","incorrect","incorrect",'incorrect']
    random.shuffle(n_list)
    if request.method == "POST":
        quiz = request.POST.get("quiz") #Grab the item from the form
        if request.POST.get('correct'): # if the user click on button that his name =correct - the choice is correct
            message = "תשובה נכונה"
            count += 1
            correct_answer +=1
            return HttpResponseRedirect("/polls/practice",{"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,"quiz":quiz})
        elif request.POST.get('incorrect'):
            count += 1
            incorrect_answer += 1
            message = "תשובה לא נכונה"
            return render(request, "practice.html", {"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess, "quiz":quiz })
        elif request.POST.get('show'):
            help = random_word_to_guess
            return HttpResponseRedirect("/polls/practice", {"help",help})

    return render(request, "practice.html", {'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,'count':count})







