from .serializers import MagazineSerializer
from rest_framework import generics
from magazines.models import MagazinePost
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


class MagazineListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MagazinePost.objects.order_by('uploaded_at')
    serializer_class = MagazineSerializer


class MagazineDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MagazinePost.objects.all()
    serializer_class = MagazineSerializer


# def detail_view(request, *args, **kwargs):
#     return HttpResponse("It is working")




