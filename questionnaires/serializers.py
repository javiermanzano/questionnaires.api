from questionnaires.models import CollectedData
from rest_framework import serializers

class CollectedDataSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = CollectedData
    fields = [
      'first_name',
      'last_name',
      'email',
      'providers',
      'created'
    ]