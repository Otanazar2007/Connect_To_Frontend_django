from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    pr_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pr_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    pr_name = models.CharField(max_length=100)
    pr_desc = models.TextField(max_length=2000)
    pr_price = models.FloatField()
    pr_count = models.IntegerField()
    pr_photo = models.FileField()
    pr_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pr_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class UserCart(models.Model):
    user_id = models.IntegerField()
    pr_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    pr_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user_id

    class Meta:
        verbose_name = 'User Cart'
        verbose_name_plural = 'User Carts'