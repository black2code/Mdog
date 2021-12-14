import json

from django.shortcuts import render
from django.http     import JsonResponse
from django.views    import View

from owners.models import *

class ownersView(View):
    def post(self, request):    
        data     = json.loads(request.body)
        Owner.objects.create(
            name = data['name'], 
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message':'created'}, status=201)


class dogsView(View):
    def post(self, request):
        data    = json.loads(request.body)
        a1 = Owner.objects.get(name=data['owner'])
        dog.objects.create(
            owner = a1,
            name = data['name'],
            age = data['age']
            
        )
        return JsonResponse({'message':'created'}, status=201)
