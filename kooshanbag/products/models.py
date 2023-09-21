from django.db import models
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200,
                            verbose_name="اسلاگ دسته بندی", unique=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name




class Color(models.Model):
    color = models.CharField(max_length=200, 
                             verbose_name="رنگ", unique=True)
    
    
    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"

    
    
    def __str__(self):
        return self.color
    


class Image(models.Model):
    image = models.ImageField(verbose_name="تصویر", 
                              upload_to="product/more/image/%y/%m/%d")
    
    
    
    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"
        



class Size(models.Model):
    size = models.CharField(max_length=200, 
                            verbose_name="سایز", unique=True) 
    
    
    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایز ها"
        
    
    def __str__(self):
        return self.size
        
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,
                                 verbose_name="دسته بندی محصول",
                                 related_name='products',
                                 on_delete=models.CASCADE)
    
    size = models.ForeignKey(Size,
                             on_delete=models.CASCADE,
                             verbose_name="سایز محصول")
    
    name = models.CharField(verbose_name="نام محصول",
                             max_length=200)
    
    slug = models.SlugField(verbose_name="اسلاگ محصول", 
                             max_length=200)
    
    
    image = models.ImageField(verbose_name="تصویر اصلی محصول",
                               upload_to='products/%Y/%m/%d', blank=True)
    
    images = models.ManyToManyField(Image, 
                                    verbose_name="تصاویر محصول")
    
    description = models.TextField(verbose_name="توضیحات محصول", blank=True)
    
    colors = models.ManyToManyField(Color, 
                                    verbose_name="رنگ های موجود محصول")
    
    price = models.IntegerField(verbose_name="قیمت محصول")
    
    quantity = models.PositiveSmallIntegerField(verbose_name="تعداد محصول")
    
    available = models.BooleanField(verbose_name="موجوده؟", default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]



    def __str__(self):
        return self.name



