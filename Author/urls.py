
from rest_framework import routers
from .views import AuthorViewSet, CompositionsViewSet

router = routers.DefaultRouter()

router.register('Authors', AuthorViewSet)
router.register('Compositions', CompositionsViewSet)

urlpatterns = router.urls