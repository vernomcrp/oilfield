from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from moneyflow import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
routers = routers.DefaultRouter()
# routers.register(r'users', UserViewSet)
routers.register(r'mrecords', views.MoneyFlowViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
