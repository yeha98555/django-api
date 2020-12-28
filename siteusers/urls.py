from django.urls import include, path
from rest_framework import routers
from siteusers.api import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, 'user')  # register api path
# router.register('accounts', AccountViewSet, 'account')

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),  # admin
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
