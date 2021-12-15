import json

from django.shortcuts import render
from django.http     import JsonResponse
from django.views    import View

from owners.models import Owner, dog

class ownersView(View):
    def post(self, request):    
        data     = json.loads(request.body)
        Owner.objects.create(
            name = data['name'], 
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message':'created'}, status=201)
    
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all().values('name', 'age')
            results.append(
                {
                    "owner name"      : owner.name,
                    "owner age"       : owner.age,
                    "email"           : owner.email,
                    "dog"             : [dog for dog in dogs]
                }
            )
        return JsonResponse({'results':results}, status=200)


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
    
    def get(self, request):
        dogs = dog.objects.all()
        results = []
        for dog1 in dogs:
            results.append(
                {
                    "owner"     : dog1.owner.name,
                    "name"      : dog1.name,
                    "age"       : dog1.age
                }
        )
        return JsonResponse({'results':results}, status=200)

