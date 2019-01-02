from informal.models import Item
from informal.models import Produto
from informal.models import Vendedor

from rest_framework import serializers


class ProdutoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produto
		fields = ('id', 'nome',)

class VendedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendedor
		fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
	produto = ProdutoSerializer()
	vendedor = VendedorSerializer()

	class Meta:
		model = Item
		fields = '__all__'