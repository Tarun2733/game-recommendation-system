from django.http import  JsonResponse
import pickle
import pandas as pd
import os
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#load pkl model
#using settings.BASE_DIR to get the path of the model

MODEL_PATH = os.path.join(settings.BASE_DIR, 'gamerecom', 'models', 'game_recommender.pkl')
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

#load data
tagged = model['tagged']
similarity_matrix = model['similarity_matrix']

#recommendation function
def recommend(game):
    g = game.lower()
    idx = tagged[tagged['name'].str.lower() == g].index[0]
    d = similarity_matrix[idx]
    lst = sorted(list(enumerate(d)), reverse=True, key=lambda x: x[1])[1:6]
    recoms = [tagged.iloc[i[0]]['name'] for i in lst]
    return recoms




# Create your views here.
@api_view(['GET'])
def recommend_game(request):
    # return HttpResponse("This is the game recommendation page.")
    game = request.GET.get('game')
    if not game:
        return JsonResponse({'error': 'No game provided'}, status=400)

    try:
        recommendations = recommend(game)
        return JsonResponse({'recommendations': recommendations})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)