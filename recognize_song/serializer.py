from rest_framework.serializers import ModelSerializer
from .models import recognize_song


class recognizeSerializer(ModelSerializer):
    class Meta:
        model = recognize_song
        fields = ['id', 'name', 'data_song']
