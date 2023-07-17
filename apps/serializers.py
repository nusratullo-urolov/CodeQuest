from rest_framework.serializers import ModelSerializer

from apps.models import Problems


class ProblemsModelSerializer(ModelSerializer):
    class Meta:
        model = Problems
        fields = '__all__'
