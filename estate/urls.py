from rest_framework.routers import DefaultRouter
from estate import views


router = DefaultRouter()
router.register('', views.EstateViewSet, basename='estate')

urlpatterns = router.urls
