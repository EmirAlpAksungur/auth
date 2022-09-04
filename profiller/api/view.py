from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from profiller.api.permissions import IsDurumSahibiOrReadOnly,IsProfilSahibiOrReadOnly
from profiller.api.serializers import ProfilSerializer,ProfilDurumSerializer
from profiller.models import Profil,ProfilDurum



class ProfileListAPIView(ListAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer


class ProfileIdListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsProfilSahibiOrReadOnly]

class ProfileStateListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProfilDurum.objects.all()
    serializer_class = ProfilDurumSerializer
    permission_classes = [IsDurumSahibiOrReadOnly]