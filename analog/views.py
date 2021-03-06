import random

from .forms import CreateWord , CreateAnalog
from .models import Analog , hebrew_words
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.

def add_analog(request):
    submitted = False
    if request.method == "POST":
        form = CreateAnalog(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_analog?submitted=True')
    else:
        form = CreateAnalog
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_analog.html', {'form': form, 'submitted': submitted})





def add_hebrew_word(request):
    submitted = False
    if request.method == "POST":
        form = CreateWord(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_hebrew_word?submitted=True')
    else:
        form = CreateWord
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_hebrew_word.html', {'form': form, 'submitted': submitted})

# def delete_hebrew_word(request,word_id):
#         word = hebrew_words.objects.filter(pk=word_id)  # Get a specific item from DB
#         word.delete()
#         return redirect("hebrew-words")


@csrf_exempt
def Show_all_hebrew_words(request):
    words_list = hebrew_words.objects.filter(approved= True)
    words_list.order_by("-pub_date")

    return render(request,"all_hebrew_words.html",{"words_list":words_list})


#
# def practice_analog(request):
#     words_list = Analog.objects.filter(approved= True)  # Take all the words that approved by the admin
#     random_word_to_guess = random.choice(words_list) # Take one random words from the DB
#     word_1 = random.choice(words_list)
#     word_2 = random.choice(words_list)
#     word_3 = random.choice(words_list)
#     quiz_list = [word_1, word_2, word_3, random_word_to_guess]
#     random_list = random.shuffle(quiz_list)
#     count = 0
#     correct_answer = 0
#     incorrect_answer = 0
#     n_list = ["correct","incorrect","incorrect",'incorrect']
#     random.shuffle(n_list)
#     if request.method == "POST":
#         quiz = request.POST.get("quiz") #Grab the item from the form
#         if request.POST.get('correct'): # if the user click on button that his name =correct - the choice is correct
#             message = "?????????? ??????????"
#             count += 1
#             correct_answer +=1
#             return HttpResponseRedirect("/polls/practice",{"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,"quiz":quiz})
#         elif request.POST.get('incorrect'):
#             count += 1
#             incorrect_answer += 1
#             message = "?????????? ???? ??????????"
#             return render(request, "practice.html", {"incorrect_answer":incorrect_answer,"correct_answer":correct_answer,'count':count,'message': message, 'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess, "quiz":quiz })
#         elif request.POST.get('show'):
#             help = random_word_to_guess
#             return HttpResponseRedirect("/polls/practice", {"help",help})
#
#     return render(request, "practice.html", {'word_1':word_1,'word_2':word_2,'word_3':word_3,'random_word_to_guess':random_word_to_guess,'count':count})
#
