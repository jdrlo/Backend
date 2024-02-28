from rest_framework import serializers

from .models import SugeQuejas

class SugeQuejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SugeQuejas
        fields = "__all__"
