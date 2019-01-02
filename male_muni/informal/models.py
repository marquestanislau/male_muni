# @author Estanislau Marques

from django.db import models



# A provincia em que se encontra o mercado
class Provincia(models.Model):
	nome = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.nome

# A cidade em que se encontra o mercado

class Cidade(models.Model):
	nome = models.CharField(max_length=100, blank=False)
	provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome
	
"""
	Os mercados nacionais registados 
	no sistema para a facil localização de cada 
	produto
"""
class Mercado(models.Model):
	nome = models.CharField(max_length=100, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

	@property
	def provincia(self):
		return cidade.provincia

# Aquele que posta os produtos
class Vendedor(models.Model):
	nome = models.CharField(max_length=50, blank=False)
	apelido = models.CharField(max_length=50, blank=False)
	contacto = models.IntegerField(blank=False)
	contacto_alternativo = models.IntegerField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


# Aquele que vai visualizar o produto no sistema
# Posteriormente ele pode decidir ir ao mercado para comprar 
class Cliente(models.Model):
	pass


# Categoria de cada produto, deve estar registado no sistema.
class Categoria(models.Model):
	nome = models.CharField(max_length=150, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome

# O que vai ser vendido pelo vendedor e comprado pelo cliente
# Os produtos são pré-registados no sistema para evitar redundância de informação
class Produto(models.Model):
	nome = models.CharField(max_length=200, blank=False)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	# Colocar a categoria de cada produto, 
	# As categorias são conforme os tipos de alimentos ou produtos
	# Inicialmente devemos pensar somente nos produtos alimenticios

	def __str__(self):
		return self.nome


class Item(models.Model):
	nome = models.CharField(max_length=100, blank=False)
	preco = models.DecimalField(max_digits=6, decimal_places=2)
	vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	
# O post irá juntar o produto, vendedor, gostos e comentarios para mostrar ao cliente
# o quão o vendedor é aceite pela comunidade de clientes que possui
class Post(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField()

# Comentario de cada cliente, pode ser positivo ou negativo
class Comentario(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)	


# Esta opção é para classificar um produto de acordo com o 
# número de gostos que receber
class Gosto(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)