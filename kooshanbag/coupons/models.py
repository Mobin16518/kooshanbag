from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(verbose_name="کد تخفیف",
                            max_length=50 , unique=True)
    
    valid_from = models.DateTimeField(verbose_name="شروع اعتبار")
    
    valid_to = models.DateTimeField(verbose_name="بایان اعتبار")
    
    discount = models.IntegerField(verbose_name="درصد تخفیف",
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)], help_text="درصد تخفیف از 0 تا 100")
    
    active = models.BooleanField(verbose_name="وضعیت")
    
    
    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کد های تخفیف"
        
        
    def __str__(self):
        return f'{self.code}'
    
    
        
    
