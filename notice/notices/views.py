from rest_framework import viewsets
from rest_framework import mixins
from .serializers import UserModelSerializer
from .models import User


# Create your views here.
class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
