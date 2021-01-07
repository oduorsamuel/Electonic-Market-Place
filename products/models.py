from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=80000)
    price = models.CharField(max_length=255)
    old_price = models.CharField(max_length=250)
    file = models.CharField(max_length=250)
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=250)
    sub_category_id = models.IntegerField()
    sub_category_name = models.CharField(max_length=250)
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=250)
    sub_category_id = models.IntegerField()
    sub_category_name = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)

    class Category(models.Model):
        name = models.CharField(max_length=255)
        is_deleted = models.BooleanField(default=False, editable=True)
        created = models.DateTimeField(auto_now_add=True)

    class SubCategory(models.Model):
        name = models.CharField(max_length=255)
        category_id = models.IntegerField()
        category_name = models.CharField(max_length=255)
        is_deleted = models.BooleanField(default=False, editable=True)
        created = models.DateTimeField(auto_now_add=True)

