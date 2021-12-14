from rest_framework import viewsets


from .models import Category, Course, Subcategory
from .serializers import CourseSerializer, CategorySerializer, SubcategorySerializer
from .filters import CourseFilter
from core.pagination import NoPagination

# Create your views here.


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = NoPagination
    queryset = Subcategory.objects.all().order_by('id')
    serializer_class = SubcategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = NoPagination
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):

    filter_class = CourseFilter
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
