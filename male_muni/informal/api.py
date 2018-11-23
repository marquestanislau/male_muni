from rest_framework import routers

from informal.views import ItemViewSet
from informal.views import ProdutoViewSet

router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('produtos', ProdutoViewSet)