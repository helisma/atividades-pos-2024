from rest_framework import serializers
from rest_framework import viewsets
from .models import Artista, Album, Musica

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    
    def getAlbum(self, instance):
        album = super().getAlbum(instance)
        # Verifica se o id do artista no álbum corresponde ao id na URL
        artista_pk = self.context.get('artista_pk')
        if artista_pk is not None and instance.artista_id != int(artista_pk):
            return {}  # Retorna um objeto vazio para álbum que não pertence ao artista
        return album

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'


    def getMusica(self, instance):
        musicas = super().getMusica(instance)
        # Verifica se o id do artista no álbum corresponde ao id na URL
        album_pk = self.context.get('album_pk')
        if album_pk is not None and instance.album_id != int(album_pk):
            return {}  # Retorna um objeto vazio para álbum que não pertence ao artista
        return musicas

    
