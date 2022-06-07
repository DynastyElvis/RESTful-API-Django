from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import items
from serializers import ItemSerializer








@api_view(['GET'])# there is post, delete, put and we need get
def getData(request):
      items = Item.objects.all()
      serializer = ItemSerializer(items, many=True)
      return Response(serializer.data)
