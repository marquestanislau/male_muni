# from django.shortcuts import render
from rest_framework import viewsets
from informal.models import Item
from informal.models import Produto

from informal.serializers import ItemSerializer
from informal.serializers import ProdutoSerializer


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()

    serializer_class = ItemSerializer


class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.all()

    serializer_class = ProdutoSerializer
