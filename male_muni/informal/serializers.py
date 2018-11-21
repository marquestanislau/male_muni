from informal.models import Item

from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'