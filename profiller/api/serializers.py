from pickle import TRUE
from profiller.models import Profil,ProfilDurum
from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profil
        fields = ["user","bio","sehir"]


"""class ProfilFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ['foto']"""


class ProfilDurumSerializer(serializers.ModelSerializer):
    user_profil = ProfilSerializer(read_only=True)

    class Meta:
        model = ProfilDurum
        fields = ["user_profil",'durum_mesaji',"yaratilma_zamani","guncelleme_zamani"]
