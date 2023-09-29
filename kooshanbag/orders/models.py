from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from products.models import Product
from coupons.models import Coupon


class Order(models.Model):
    user = models.ForeignKey(User,
                             related_name="user_orders",
                             on_delete=models.CASCADE, verbose_name="کاربر")
    f_name = models.CharField(max_length=50,
                                  verbose_name="نام")
    l_name = models.CharField(max_length=50,
                              verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن", null=True)
    address = models.CharField(max_length=250, 
                               verbose_name="آدرس")
    postal_code = models.CharField(max_length=20,
                                   verbose_name="کد بستی")
    city = models.CharField(max_length=100, 
                            verbose_name="شهر")
    created = models.DateTimeField(auto_now_add=True, 
                                   verbose_name="ایجاد شده")
    updated = models.DateTimeField(auto_now=True, 
                                   verbose_name="آبدیت شده")
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               null=True,blank=True,
                               related_name='orders',
                               verbose_name="کوبون",
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                       MaxValueValidator(100)], verbose_name="درصد تخفیف")
    total_price = models.BigIntegerField(verbose_name="قیمت")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / int(100))
        return int(0)

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()



class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='order',
                              verbose_name="سفارش",
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='order_items',
                                verbose_name="محصولات سفارش")
    price = models.BigIntegerField(verbose_name="قیمت")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity