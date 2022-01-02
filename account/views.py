import json

from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Create your views here.
def get_crsf(request):
    response = JsonResponse({"Info": "Success - Set CRSF cookie"})
    response["X-CRSFToken"] = get_token(request)
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"info": "Username and Password are requried"})

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"info": "Username does not exist"}, status=400)
    login(request, user)
    return JsonResponse({"info": "User logged in successfully"})

def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})

class SessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})
