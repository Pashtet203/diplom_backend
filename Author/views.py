from .models import Author, Composition
from rest_framework.viewsets import ModelViewSet
from .serializer import AuthorSerializer, CompositionsSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CompositionsViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionsSerializer


