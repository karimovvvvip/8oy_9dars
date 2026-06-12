from rest_framework.viewsets import ModelViewSet

from .models import Actor, Directory, Genre, Movie, Comment
from .serializers import (ActorSerializer, GenreSerializer, MovieSerializer,
                          DirectorySerializer, ActorAdminSerializer, MovieAdminSerializer, CommentSerializer)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import MyIsAuthenticatedOrReadOnly, IsOwner

class GenreSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ActorSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class DirectorySet(ModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class MovieSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class CommentSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [MyIsAuthenticatedOrReadOnly, ]