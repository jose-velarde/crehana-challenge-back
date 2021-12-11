from django.urls import path, include
from rest_framework.routers import DefaultRouter
from celerative_task1 import views

app_name = "celerative_task1"

router = DefaultRouter()
router.register(r'person', views.PersonViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]