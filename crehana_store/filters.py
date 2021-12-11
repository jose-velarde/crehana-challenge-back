import django_filters as filters
from django.db.models import F

from .models import Course


class CourseFilter(filters.FilterSet):
    price_gte = filters.CharFilter(label="price is greater than", field_name="real_price", method="filter_price_gte")
    price_lte = filters.CharFilter(label="price is lower than", field_name="real_price", method="filter_price_lte")

    class Meta:
        model = Course
        fields = {
            "level": ["exact", "startswith"],
            "category__category_name": ["exact", "startswith"],
            "subcategory__subcategory_name": ["exact", "startswith"],
        }

    def filter_price_gte(self, qs, name, value):
        return qs.filter(real_price__gte=F("real_price") - F("real_price") * F("discount") / 100 + value)

    def filter_price_lte(self, qs, name, value):
        return qs.filter(real_price__lte=F("real_price") - F("real_price") * F("discount") / 100 + value)
