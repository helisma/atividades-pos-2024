from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets #conjunto de views  ue o rest_frm vai criar
from .models import Artista, Album, Musica
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Artistas
    """
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """
    serializer_class = AlbumSerializer
    def get_queryset(self):
        artista_pk = self.kwargs.get('artista_pk')
        if artista_pk:
            return Album.objects.filter(artista_id=artista_pk)
        return Album.objects.all()

class MusicaViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    serializer_class = MusicaSerializer
    def get_queryset(self):
        album_pk = self.kwargs.get('album_pk')
        if album_pk:
            return Musica.objects.filter(album_id=album_pk)
        return Musica.objects.all()
