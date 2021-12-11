from django.db import models


class Category(models.Model):
    id = models.IntegerField()
    category_name = models.CharField(primary_key=True, max_length=254)

    def __str__(self):
        return "{}".format(self.category_name)
    class Meta:
        verbose_name_plural = "categories"

class Subcategory(models.Model):
    id = models.IntegerField()
    subcategory_name = models.CharField(primary_key=True, max_length=254)
    category = models.ForeignKey(Category, to_field="category_name", db_column="category", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.subcategory_name)
    class Meta:
        verbose_name_plural = "subcategories"


class Course(models.Model):
    course_name = models.CharField(max_length=254)
    category = models.ForeignKey(Category, to_field="category_name", db_column="category", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, to_field="subcategory_name", db_column="subcategory", on_delete=models.CASCADE)
    level = models.CharField(max_length=254)
    username = models.CharField(max_length=254)
    real_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    course_score = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.IntegerField()

    def __str__(self):
        return "{}".format(self.course_name)
