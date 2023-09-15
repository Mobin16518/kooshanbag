from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200,
                            verbose_name="اسلاگ دسته بندی", unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 verbose_name="دسته بندی محصول",
                                 related_name='products',
                                 on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name="نام محصول",
                             max_length=200)
    
    slug = models.SlugField(verbose_name="اسلاگ محصول", 
                             max_length=200)
    
    
    image = models.ImageField(verbose_name="تصویر اصلی محصول",
                               upload_to='products/%Y/%m/%d', blank=True)
    
    description = models.TextField(verbose_name="توضیحات محصول", 
                                    blank=True)
    
    price = models.IntegerField(verbose_name="قیمت محصول")
    
    quantity = models.PositiveSmallIntegerField(verbose_name="تعداد محصول")
    
    available = models.BooleanField(verbose_name="موجوده؟", default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])