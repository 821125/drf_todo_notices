from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Project, TODO
from notices.models import User


class UsersListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ProjectNameSerializer(ModelSerializer):
    users_list = UsersListSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name',)


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(HyperlinkedModelSerializer):
    project = ProjectNameSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
