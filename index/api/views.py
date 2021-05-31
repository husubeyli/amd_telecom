import json
from django.views.generic import View
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.http import HttpResponse
from .serializers import SubscriberSerializer
from django.shortcuts import render
from product.models import Product
from ..signals import send_subscribe_mail


class SubscribeView(View):
    
    # permission_class = (AllowAny,)
    def post(self, request):

        data = json.loads(request.body)
        print(data['email'], 'datalar')
        serializer = SubscriberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_subscribe_mail(data['email'])
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    


