from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import FormSerializer, UpdateSerializer
from django.http import HttpResponse

# def completePayment(request):
#     return HttpResponse('Payment Successful')

@api_view(['GET','POST'])
def yogaform(request):
    if request.method=='POST':
        serializer=FormSerializer(data=request.data)
        if serializer.is_valid():
           FormSerializer.save(request.data)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    return HttpResponse('OK')

@api_view(['GET','POST'])
def updateform(request):
    if request.method=='POST':
        serializer=UpdateSerializer(data=request.data)
        if serializer.is_valid():
           UpdateSerializer.save(request.data)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    return HttpResponse('OK')

@api_view(['GET','POST'])
def completePayment(request):
    if request.method == 'POST':
        return HttpResponse('Payment Successful')
    return HttpResponse('OK')