from django.contrib import admin

# Local imports from app informal
from informal.models import Cidade
from informal.models import Mercado
from informal.models import Provincia
from informal.models import Categoria
from informal.models import Produto
from informal.models import Item
from informal.models import Vendedor

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'provincia')


@admin.register(Mercado)
class MercadoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cidade', 'created')
# admin.site.register(Mercado)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'categoria')


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'created', 'modified',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('nome', 'preco',)


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'apelido', 'contacto', 'contacto_alternativo', 'mercado',)


