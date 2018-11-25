from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from informal.models import Produto
from informal.serializers import ProdutoSerializer

class ProdutoViewTest(APITestCase):

	client = APIClient()

	@staticmethod
	def create_product(nome = ""):

		if nome != "":
			Produto.objects.create(nome = nome)


	def setUp(self):
		self.create_product(nome="Laranja")
		self.create_product(nome="Morango")
		self.create_product(nome="Cacana")


class AllProdutosTest(ProdutoViewTest):

	def get_all_products(self):

		response = self.client.get(
			reverse("produtos", kwargs={"version": "v1"})
		)

		produto = Produto.objects.all()

		serialized = ProdutoSerializer(produto, many=True)

		self.assertEqual(response.data, serialized.data)
		self.assertEqual(reponse.status_code, status.HTTP_200_OK)

