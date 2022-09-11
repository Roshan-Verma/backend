from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie


def alluser(request):
    if request.method == 'GET':
        users = User.objects.all()
        users = list(users.values())
        return JsonResponse(users, safe=False)
    else:
        response = JsonResponse({'message': 'Hello, World!'})
        return response

class Login(View):
    @csrf_exempt
    # @ensure_csrf_cookie
    def login(request):
        if request.method == 'POST':
            anwesha_id  = request.POST.get('anwesha_id')
            password = request.POST.get('password')
            user = User.objects.filter(anwesha_id =anwesha_id , password=password)
            if user:
                this_user = list(User.objects.get(anwesha_id =anwesha_id , password=password))
                return JsonResponse(this_user)
            else:
                return JsonResponse({'message': 'Invalid Anwesha ID or Password'})
        else:
            return JsonResponse({'message': 'Invalid Request'})



@csrf_exempt
# @ensure_csrf_cookie
def logout(request):
        if request.method == 'POST':
            request.session.clear()
            return JsonResponse({'message': 'Logout Successful'})
        else:
            return JsonResponse({'message': 'Invalid Request'})
