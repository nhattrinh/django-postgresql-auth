from django.contrib.auth import authenticate
from auth_api.models import User
from django.http import JsonResponse
import json
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def register(request):
    if request.method == 'POST':
        username = request.REQUEST.get('username', None)
        email = request.REQUEST.get('email', None)
        password = request.REQUEST.get('password', None)

        if username and email and password:
            user = User.objects.create_user(username, email, password)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            user.save()

            return JsonResponse({
                'keys': [
                    { 'success': True },
                    { 'user': json.dumps(user) },
                    { 'token': json.dumps(token) },
                    { 'msg': 'Successfully created a new user' }
                ]
            })
    
    return JsonResponse({
        'keys': [
            { 'success': False },
            { 'msg': 'Invalid request made, try again' }
        ]
    })

def login(request):
    if request.method == 'POST':
        username = request.REQUEST.get('username', None)
        password = request.REQUEST.get('password', None)

        if username and password:
            user = authenticate(request)
            if user is None:
                return JsonResponse({
                    'keys': [
                        { 'success': False },
                        { 'msg': 'Invalid credentials, try again' } 
                    ]
                });
            else:
                return JsonResponse({
                    'keys': [
                        { 'success': True },
                        { 'msg': 'User successfully logged in' }
                    ]
                })
    return JsonResponse({
        'keys': [
            { 'success': True },
            { 'msg': 'Invalid request made, try again' }
        ]
    })