from django.contrib import admin

# Local imports from app informal
from informal.models import Cidade
from informal.models import Mercado
from informal.models import Provincia
from informal.models import Categoria
from informal.models import Produto

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

admin.site.register(Provincia)
admin.site.register(Categoria)


