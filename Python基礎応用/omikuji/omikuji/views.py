
from random import choice

from django.http import HttpResponse

def index(reqesut):
    
    omikuji = ["大吉","中吉","小吉","凶"]
    
    result = choice(omikuji)
    
    responseobject = HttpResponse(result)
    return responseobject