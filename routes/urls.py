from rest_framework import routers
from .views import RouteViewSet

router = routers.DefaultRouter()
router.register(r"routes", RouteViewSet)
urlpatterns = router.urls
