from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         return HttpResponse('len is {}' .format(len(name)))
#     return HttpResponse('It is GET request')
#
# def index2(request):
#     age = int(request.POST.get('age'))
#     if age < 18:
#         return HttpResponse('Closed')
#     else:
#         return HttpResponse('Welcome')

def cw18_index_01(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        amount_vowels = 0
        amount_consonant = 0
        vowels = 'eyuioa'
        consonant = 'qwrtpsdfghjklzxcvbnm'
        for i in 'comment':
            if i in vowels:
                amount_vowels += 1
            if i in consonant:
                amount_consonant += 1
        result = 'len is {}, amount_vowels is {}, amount_consonant is {}' .format(len(comment), amount_vowels, amount_consonant)
        return HttpResponse(result)
    return HttpResponse('It is GET request')