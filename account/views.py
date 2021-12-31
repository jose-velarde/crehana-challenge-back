import json

from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST


# Create your views here.
def get_crsf(request):
    response = JsonResponse({"Info": "Success - Set CRSF cookie"})
    response["X-CRSFToken"] = get_token(request)
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response


@require_POST
def loginView(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"info": "Username and Password are requried"})
    
    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"info": "Username does not exist"}, status=400)
    login(request, user)
    return JsonResponse({"info":"User logged in successfully"})

# class WhoamiViewSet(viewsets.ViewSet):
#     serializer_class = WhoamiSerializer
