from django import template
import random
register = template.Library()

@register.filter
def shuffle(arg):
    tmp = list(arg)
    random.shuffle(tmp)

@register.filter
def choice(arg):
    tmp = list(arg)
    take_one = random.choice(tmp)
    tmp.remove(take_one)
    return random.choice(tmp)

@register.filter
def index(arg):
    tmp = list(arg)
    return tmp[0]

@register.filter
def index_2(arg):
    tmp = list(arg)
    return tmp[1]

@register.filter
def index_3(arg):
    tmp = list(arg)
    return tmp[2]

@register.filter
def index_4(arg):
    tmp = list(arg)
    return tmp[3]



    # my_list =  ['<input name = "incorrect" type="submit" value={{word_1.Hebrew_word}} class="btn btn-primary"/>',
    # '<input name = "incorrect" type="submit" value={{word_2.Hebrew_word}} class="btn btn-primary"/>',
    # '<input name = "incorrect" type="submit" value={{word_3.Hebrew_word}} class="btn btn-primary"/>',
    # '<input name = "correct" type="submit" value={{random_word_to_guess.Hebrew_word}} class="btn btn-primary"/>']