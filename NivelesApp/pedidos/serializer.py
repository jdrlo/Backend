from rest_framework import serializers

from pedidos.models import Pedido_Mesero,Pedido_Bodega,Inventario

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Mesero
        fields = "__all__"

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Bodega
        fields = "__all__"

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"