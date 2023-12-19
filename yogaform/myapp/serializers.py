from .models import *
from rest_framework import serializers

class FormSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    contact_number = serializers.CharField() 
    gender=serializers.CharField()
    batch_id=serializers.IntegerField()
    amount=serializers.IntegerField()
    payment_successful=serializers.BooleanField()

    def save(self):
        f_name=self.get('first_name')
        l_name=self.get('last_name')
        a=self.get('age')
        e=self.get('email')
        cn=self.get('contact_number')
        g=self.get('gender')
        b=self.get('batch_id')
        amt=self.get('amount')
        p=self.get('payment_successful')
        User.objects.create(first_name=f_name,last_name=l_name,age=a,email=e,contact_number=cn,gender=g, batch_id=b)
        obj=User.objects.filter(email=e)[0]
        u_id=obj
        Payment.objects.create(user_id=u_id,amount=amt,payment_successful=p)
        if(p=='True'):
            o=Payment.objects.filter(user_id=u_id)[0]
            p_id=o
            Admission.objects.create(payment_id=p_id,user_id=u_id,batch_id=b)

class UpdateSerializer(serializers.Serializer):
    email=serializers.EmailField()
    batch_id=serializers.IntegerField()
    payment_successful=serializers.BooleanField()

    def save(self):
        e=self.get('email')
        b=self.get('batch_id')
        p=self.get('payment_successful')
        amt=self.get('amount')
        User.objects.filter(email=e).update(batch_id=b)
        obj=User.objects.filter(email=e)[0]   
        u_id=obj
        Payment.objects.create(user_id=u_id,amount=amt,payment_successful=p)
        if(p=='True'):
            o=Payment.objects.filter(user_id=u_id)[0]
            p_id=o
            Admission.objects.create(payment_id=p_id,user_id=u_id,batch_id=b)