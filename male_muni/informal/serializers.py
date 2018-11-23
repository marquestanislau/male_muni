from informal.models import Item
from informal.models import Produto

from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Produto
		fields = ('id', 'nome',)


