from rest_framework import serializers

from .models import Category, Course, Subcategory

class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.ReadOnlyField(source='category.category_name')

    class Meta:
        model = Subcategory
        fields = (
            "id",
            "subcategory_name",
            "category",
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "category_name",
        )


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(source='category.category_name')
    subcategory = serializers.ReadOnlyField(source='subcategory.subcategory_name')

    class Meta:
        model = Course
        fields = (
            "id",
            "course_name",
            "category",
            "subcategory",
            "level",
            "username",
            "real_price",
            "discount",
            "price",
            "course_score",
            "users",
        )

    def get_price(self, obj):
        return round((obj.real_price * obj.discount) / 100, 2)
