from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import book
from .serializers import bookserializer

# Create your views here.

@api_view(['GET' , 'POST', 'PUT' ,'PATCH','DELETE'])
def book_api(request , pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            boo = book.objects.get(id=id)
            serializer = bookserializer(boo)
            return Response(serializer.data)

        boo = book.objects.all()
        serializer = bookserializer(boo , many = True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = bookserializer(data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id=pk
        boo = book.objects.get(pk=id)
        serializer = bookserializer(boo , data = request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)   

    if request.method == 'PATCH':
        id=pk
        boo = book.objects.get(pk=id)
        serializer = bookserializer(boo , data = request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated PARTIALLY'})
        return Response(serializer.errors)   


    if request.method == 'DELETE':
        id=pk
        boo = book.objects.get(pk=id)
        boo.delete()
        return Response({'msg':'Data DELETED'})