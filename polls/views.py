import random
import time

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Words
from django.http import HttpResponseRedirect
from .forms import WordForm

# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


def search_function(request):
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



@csrf_exempt
def add_word(request):
    submitted = False
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_word?submitted=True')
    else:
        form = WordForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_word.html', {'form': form, 'submitted': submitted})



@csrf_exempt
def Show_all_words(request):
    words_list = Words.objects.filter(approved= True).order_by("English_word")
    count = Words.objects.all().count()
    words_list.order_by("-pub_date")
    return render(request,"all_words.html",{"words_list":words_list})



def Search_word(request):
    x = False
    count = Words.objects.all().count()
    if request.method == "POST":
        search = request.POST.get("search") #Grab the search item
        word = Words.objects.filter(English_word__iexact =search, approved= True)
        if word.exists():
            return render(request,"search_page.html", {'search': search, 'word': word, "count":count})
        if not word:
            x = True
            message = f" עדיין לא קיימת במאגר \n להוספת המילה למאגר לחץ כאן {search}  המילה "
            return render(request,"search_page.html", {'message': message, "count":count, 'x':x})
    else:
        return render(request, "search_page.html", {"count": count})






def practice(request):
    words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
    four_options = [random.choice(words_list) for i in range(4)]

    x = four_options[0]
    z = x.Hebrew_word
    random.shuffle(four_options)
    choice_user = request.POST.get("quiz")
    choice_1 = str(choice_user)
    word = z[:4]
    choice = choice_1[:4]


    if request.method == "POST":

        if choice == word:
            message = f'Correct {choice} == {word}'
            return render(request, "practice.html",
                          {"four_options": four_options, "x": x, "z": z, "choice": choice, 'word': word,"message":message})
        if choice != word:
           message = f'Incorrect {choice} != {word}'
           return render(request, "practice.html",
                          {"four_options": four_options, "x": x, "z": z,  "choice": choice, 'word': word,"message":message})

    return render(request, "practice.html", {"four_options": four_options, "z": z, "x": x,})




#
# def practice(request):
#     form = QuizFrom(request.POST)
#
#     return render(request, "practice.html", {'form':form})
#
# def practice(request):
#     words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
#     random_word_to_guess = random.choice(words_list) # Take one random words from the DB
#     r_english_word = random_word_to_guess.English_word
#     r_hebrew_word = random_word_to_guess.Hebrew_word
#     word_1 = random.choice(words_list)
#     word_2 = random.choice(words_list)
#     word_3 = random.choice(words_list)
#     h_word_1 = word_1.Hebrew_word
#     h_word_2 = word_2.Hebrew_word
#     h_word_3 = word_3.Hebrew_word
#
#     quiz_list = [h_word_1, h_word_2, h_word_3,r_english_word]
#     random.shuffle(quiz_list)
#
#     count = 0
#     correct_answer = 0
#     incorrect_answer = 0
#     n_list = ["incorrect","incorrect","incorrect",'incorrect']
#     if request.method == "POST":
#         quiz = request.POST.get("correct")  # Grab the item from the form
#
#         if request.POST.get("correct") == r_hebrew_word:   # if the user click on button that his name =correct - the choice is correct
#             message = "תשובה נכונה"
#             count += 1
#             correct_answer +=1
#             return render(request, "practice.html", {"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess })
#         if request.POST.get('correct') != r_hebrew_word :
#             count += 1
#             incorrect_answer += 1
#             message = "תשובה לא נכונה"
#             return render(request, "practice.html", {"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess })
#         if request.POST.get('show'):
#             help = random_word_to_guess
#             return HttpResponseRedirect("/polls/practice", {"help",help})
#
#     return render(request, "practice.html", {'n_list':n_list,'quiz_list':quiz_list,'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,'count':count})
#
