from django.http import request
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

# Create your views here.
def get_crsf(request):
    response = JsonResponse({"Info": "Success - Set CRSF cookie"})
    response["X-CRSFToken"] = get_token(request)
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response

# class LoginViewSet(viewsets.ViewSet):
#     serializer_class = LoginSerializer


# class WhoamiViewSet(viewsets.ViewSet):
#     serializer_class = WhoamiSerializer
