from django.db.models.signals import pre_save 
from .models import Order
from django.dispatch import receiver 
import random, string

sr = random.SystemRandom()

@receiver(pre_save ,sender = Order)
def create_order_code(sender, instance, *args, **kwargs):
	code = "".join(sr.choices(string.ascii_letters ,k=5))
	code+= "".join(sr.choices(string.digits), k=3)
	instance.order_code = code
	