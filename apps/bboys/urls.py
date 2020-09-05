from rest_framework import routers

from .viewsets import BboyViewSet, CrewViewSet, CityViewSet

router = routers.SimpleRouter()
router.register('bboys', BboyViewSet)
router.register('crews', CrewViewSet)
router.register('city', CityViewSet)

urlpatterns = router.urls