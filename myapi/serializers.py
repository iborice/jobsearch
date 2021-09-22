from rest_framework import serializers
from .models import Annonce, Categorie, Forme, Poste, Ville

class AnnonceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Annonce
        fields = ('name','alias')

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ('intitule',)

class VilleSerializer(serializers.ModelSerializer):
    intitule = serializers.CharField(max_length=60, allow_blank=False)
    class Meta:
        model = Ville
        fields = ('intitule',)

class FormeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forme
        fields = ('intitule',)

class PosteSerializer(serializers.HyperlinkedModelSerializer):
    annonce = AnnonceSerializer(read_only=True)
    villes = VilleSerializer(read_only=True, many=True)
    categories = CategorieSerializer(read_only=True, many=True)
    forme = FormeSerializer(read_only=True)
    class Meta:
        model = Poste
        fields = ('annonce','intitule','forme','date','date_expiration','date_publication','description','nombre','categories','villes')


