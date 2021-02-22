import csv
from django.http import HttpResponse
from questionnaires.models import CollectedData
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer
from questionnaires.serializers import CollectedDataSerializer

class CollectedDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collected data to be viewed or edited.
    """
    queryset = CollectedData.objects.all().order_by('-created')
    serializer_class = CollectedDataSerializer
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVRenderer,)