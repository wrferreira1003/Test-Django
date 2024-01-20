from ninja import NinjaAPI
from django.http import JsonResponse
api = NinjaAPI()

@api.get('teste/')
def teste(request):
    return JsonResponse({'teste': 1})
