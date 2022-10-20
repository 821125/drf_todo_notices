from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .models import Project, TODO


# Create your views here.
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_fields = ['name']


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOLimitOffsetPagination
    filterset_fields = ['project', 'create_at', 'update_at']

    def destroy(self, request, *args, **kwargs):
        todo = TODO.objects.get(id=int(self.kwargs['pk']))
        todo.is_active = False
        todo.save()
        serializer = TODOModelSerializer(todo)
        return Response(serializer.data)
