from django.shortcuts import render
from rest_framework import viewsets
from informal.models import Item

from informal.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer