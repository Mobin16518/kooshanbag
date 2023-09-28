from django.db import models
from account.models import User


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
    
    
    image_1 = models.ImageField(verbose_name="تصویر اصلی محصول",
                               upload_to='products/%Y/%m/%d', null=True)
    
    image_2 = models.ImageField(verbose_name="تصویر دوم محصول",
                               upload_to='products/%Y/%m/%d', null=True)
    
    description = models.TextField(verbose_name="توضیحات محصول", null=True)
    
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






class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="کاربر", related_name="comments", null=True, blank=True)
    
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="محصول", related_name="comments", null=True, blank=True)
    
    comment = models.TextField(verbose_name="نظر کاربر")
    
    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now=True)
    
    
    
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرها"
        
        
        
    def __str__(self):
        return f'{self.user.phone}----{self.product.name}'
    



class ProductDescription(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="محصول", related_name="product_descriptions", null=True, blank=True)
    
    description = models.TextField(verbose_name="توضیحات")
    
    class Meta:
        verbose_name = "توضیحات محصول"
        verbose_name_plural = "توضیحات محصولات"
        
    def __str__(self):
        return self.product.name
    
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="محصول", related_name="product_images", null=True, blank=True)
    image = models.ImageField(verbose_name="تصویر", upload_to='products/images/%Y/%m/%d')
    
    
    class Meta:
        verbose_name ="تصویر محصولات"
        verbose_name_plural = "تصاویر محصولات"
        
    
    def __str__(self):
        return f'{self.product.name}'
    
    
    
class Price(models.Model):
    min_price = models.BigIntegerField(verbose_name="شروع قیمت")
    max_price = models.BigIntegerField(verbose_name="اتمام قیمت")
    
    
    class Meta:
        verbose_name ="قیمت"
        verbose_name_plural = "قیمت ها"
    
    
    