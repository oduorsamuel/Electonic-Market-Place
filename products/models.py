from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=250)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=80000)
    price = models.CharField(max_length=255)
    old_price = models.CharField(max_length=250)
    file = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=250)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False, editable=True)
    created = models.DateTimeField(auto_now_add=True)
