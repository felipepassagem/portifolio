from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import ProjectViewSet, MeViewSet, TecViewSet, CarouselViewSet


router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('me', MeViewSet, basename='me')
router.register('tec', TecViewSet, basename='tec')
router.register('carousel', CarouselViewSet, basename='carousel')


urlpatterns = [
  
  path('api/', include(router.urls)),

]