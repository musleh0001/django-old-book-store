from django.db import models
from dashboard.models import Book
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
User = get_user_model()


class OrderSingleProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.quantity} of {self.product}"

    def get_product_price(self):
        return (self.quantity*self.product.price)


    def get_product_quantity(self):
            return (self.quantity)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderSingleProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress', null=True, blank=True,
                                        on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username}'s order"

    def total_quantity(self):
        total = 0
        for q in self.products.all():
            total += int(q.get_product_quantity())
        return total

    def get_total_bill(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_product_price()
        return total


class BillingAddress(models.Model):
    PAYMENT_CHOICES = (
    ('Cash On Delivery',"Cash On Delivery"),
    ('Credit Card/Master Card',"Credit Card/Master Card"),
    ('Paypal','Paypal'),
    ('Payoneer','Payoneer'),
    
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    apartment_address = models.CharField(max_length=200)
    country = models.CharField(max_length=20)
    payment_choice = models.CharField(choices=PAYMENT_CHOICES, default="Credit Card/Master Card", max_length=30)    
    zipcode = models.CharField(max_length=5)
    save_info = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Billing Address"


class Payment(models.Model):
    PAYMENT_CHOICES = (
    ('Cash On Delivery',"Cash On Delivery"),
    ('Credit Card/Master Card',"Credit Card/Master Card"),
    ('Paypal','Paypal'),
    ('Payoneer','Payoneer'),
    
)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    choice = models.CharField(choices=PAYMENT_CHOICES, default="Credit Card/Master Card", max_length=30)
    status = models.BooleanField(default=False)
    issued = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now_add=True)