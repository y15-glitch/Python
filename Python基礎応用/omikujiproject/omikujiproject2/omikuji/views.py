
from django.http import HttpResponse

from random import choice

def index(request):
    
    omikuji = ['大吉','中吉','小吉','凶']
    
    result = choice(omikuji)
    
    responseobject = HttpResponse(result)
    return responseobject
