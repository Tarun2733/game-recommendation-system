from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recommend_game(request):
    return HttpResponse("This is the game recommendation page.")