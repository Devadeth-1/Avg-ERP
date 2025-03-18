# Incentives named App Views are here:

from rest_framework import generics
from .models import Incentive
from .serializers import IncentiveSerializer

class IncentiveListCreateView(generics.ListCreateAPIView):
    queryset = Incentive.objects.all()
    serializer_class = IncentiveSerializer
