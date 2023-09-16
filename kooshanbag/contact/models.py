from django.db import models




class Contact(models.Model):
    phone = models.CharField(max_length=11,
                             verbose_name="شماره تلفن")
    
    email = models.EmailField(verbose_name="ایمیل")
    
    adress = models.CharField(max_length=200, 
                              verbose_name="آدرس")
    
    instagram = models.URLField(verbose_name="لینک بیج اینستا")
    
    
    
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس ها"
        
    
    def __str__(self):
        return self.email
    
    



class UserContact(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="نام کاربر")
    
    email = models.EmailField(verbose_name="ایمیل کاربر")
    
    phone = models.CharField(max_length=11,
                             verbose_name="شماره تماس کاربر")
    
    title = models.CharField(max_length=200, 
                             verbose_name="موضوع")
     
    text = models.TextField(verbose_name="متن")
    
    
    
    class Meta:
        verbose_name = "تماس کاربر"
        verbose_name_plural = "تماس های کاربر"
        
        
        
    def __str__(self):
        return f'{self.name}---{self.phone}'
    