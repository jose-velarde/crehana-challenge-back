from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "crehana_store"

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubcategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
