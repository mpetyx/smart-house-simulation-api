__author__ = 'mpetyx'


from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Serializers define the API representation.
class PlugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plug
        fields = (['description'])

# ViewSets define the view behavior.
class PlugViewSet(viewsets.ModelViewSet):
    queryset = Plug.objects.all()
    serializer_class = PlugSerializer

# Serializers define the API representation.
class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('description','id','label')

# ViewSets define the view behavior.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Serializers define the API representation.
class CounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counter
        fields = (['description'])

# ViewSets define the view behavior.
class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer