from rest_framework.serializers import ModelSerializer
from .models import Author, Composition


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'years_of_life', 'img_path', 'author_info', 'listCompositions']


class CompositionsSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields = ['id', 'name', 'song_path']