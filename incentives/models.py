#Incentives named app Models.py are here:

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Incentive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_awarded = models.DateField(auto_now_add=True)
