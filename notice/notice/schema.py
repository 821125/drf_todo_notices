import graphene
from graphene_django import DjangoObjectType
from todo.models import Project, TODO
from notices.models import User


class TodoType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class CustomUserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todo = graphene.List(TodoType)
    all_users = graphene.List(CustomUserType)
    all_projects = graphene.List(ProjectType)

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)