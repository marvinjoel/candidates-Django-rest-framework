from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from candidates.presidency.models import PresidencyModel
from candidates.presidency.serializers import PresidencyModelSerailizer


class CandidatesViewset(ModelViewSet):
    queryset = PresidencyModel.objects.all()
    serializer_class = PresidencyModelSerailizer



