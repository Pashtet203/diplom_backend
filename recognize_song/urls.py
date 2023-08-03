from rest_framework import routers
from .views import recognizeViewSet
router = routers.DefaultRouter()

# router.register('recognize', recognizeViewSet.as_view())

# urlpatterns = router.urls