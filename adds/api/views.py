from .serializers import AddSerializer
from rest_framework import generics
from adds.models import Add
from rest_framework.permissions import IsAuthenticated


class AddListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Add.objects.order_by('priority')
    serializer_class = AddSerializer

