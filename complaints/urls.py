from .views import ComplaintViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"complaints", ComplaintViewSet)
urlpatterns = router.urls
