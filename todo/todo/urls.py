from django.contrib import admin
from django.urls import path, include
from my_list.views import my_list, MyListViewSet
from before_i_die.views import before_i_die, BeforeIDieViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mylist', MyListViewSet)
router.register(r'beforeidie', BeforeIDieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_list, name='mylist'),
    path('beforeidie', before_i_die, name='beforeidie'),
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
