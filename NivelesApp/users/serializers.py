from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import User, Clientes
from rest_framework import authentication

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','email', 'password', 'cargo', 'name', 'apellido_Usuario', 'genero_Usuario', 'cedula',
                'telefono']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'read_only': True}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user 
    
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            raise serializers.ValidationError('No se puede autenticar', code='authorization')
        
        data['user'] = user
        
        return data
    
class ClienteSerializer(serializers.ModelSerializer):
    id_User = UserSerializer()
    class Meta:
        model = Clientes
        fields = '__all__' 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        
        organized_data = {
            'name': representation['id_User']['name'],
            'apellido_Usuario': representation['id_User']['apellido_Usuario'],
            'imagen_Usuario': representation['imagen_Usuario'],
            'telefono': representation['id_User']['telefono'],
            'match': representation['match'],
            'estado_Civil': representation['estado_Civil']
            
        }

        return organized_data
    
    
    
class PerfilSerializer(serializers.ModelSerializer):
    id_User = UserSerializer()
    class Meta:
        model = Clientes
        fields = '__all__' 
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        
        organized_data = {
            'id_User' : representation ['id_User']['id'] ,
            'id_Cliente' : representation['id_Cliente'],
            'name': representation['id_User']['name'],
            'apellido_Usuario': representation['id_User']['apellido_Usuario'],
            'cedula': representation['id_User']['cedula'],
            'email': representation['id_User']['email'],
            'imagen_Usuario': representation['imagen_Usuario'],
            'telefono': representation['id_User']['telefono'],
            'match': representation['match'],
            'estado_Civil': representation['estado_Civil']
            
        }

        return organized_data
    
    