from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validate_age(value):
    if value < 18 or value > 65:
        raise ValidationError(('%(value)% should be between 18 and 56'), 
        params= {'age':value},) 

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.PositiveIntegerField(validators=[validate_age])
    email=models.EmailField(max_length=50,unique='True')

    contact_number = models.CharField(max_length=10, blank=True,unique='True') 

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    batch=models.ForeignKey('Batch',on_delete=models.CASCADE,null=False)

class Batch(models.Model):
    batch_id=models.AutoField(primary_key=True)
    SESSION_CHOICES = (
        ('M1', '6-7 AM'),
        ('M2', '7-8 AM'),
        ('M3', '8-9 AM'),
        ('E', '5-6 PM')
    )
    time=models.CharField(max_length=20, choices=SESSION_CHOICES)

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(null=False)
    date=models.DateTimeField(auto_now_add=True)
    payment_successful=models.BooleanField()

class Admission(models.Model):
    admission_id=models.AutoField(primary_key=True)
    payment_id=models.ForeignKey('Payment',on_delete=models.CASCADE,null=False)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE,null=False)
    batch=models.ForeignKey('Batch',on_delete=models.CASCADE,null=False)