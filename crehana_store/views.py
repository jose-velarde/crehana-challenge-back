from core.pagination import NoPagination
from rest_framework import authentication, permissions, viewsets
from django.views.decorators.csrf import ensure_csrf_cookie

from .filters import CourseFilter
from .models import Category, Course, Subcategory
from .serializers import (
    CategorySerializer,
    CourseSerializer,
    SubcategorySerializer,

)

# Create your views here.

class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = NoPagination
    queryset = Subcategory.objects.all().order_by("id")
    serializer_class = SubcategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = NoPagination
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):

    filter_class = CourseFilter
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
