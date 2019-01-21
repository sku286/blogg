from django.shortcuts import render
from sblog.serializers import CreateDataSerializer
from sblog.models import Createdata
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class CreateDataApiView(ListCreateAPIView):
    #queryset = Createdata.objects.all()
    serializer_class = CreateDataSerializer

    def get_queryset(self):
        return Createdata.objects.all()


