from rest_framework.views import APIView
from .models import recognize_song
from .serializer import recognizeSerializer
from rest_framework.response import Response
import asyncio
from shazamio import Shazam

async def Myshazam(path):
    shazam = Shazam()
    out = await shazam.recognize_song(path)
    return out

class recognizeViewSet(APIView):
    queryset = recognize_song.objects.all()
    serializer_class = recognizeSerializer
    def post(self, request):
        data  = request.FILES['data_song']
        temp = data.read()
        data.close()
        return Response({'title':asyncio.run(Myshazam(temp))})

