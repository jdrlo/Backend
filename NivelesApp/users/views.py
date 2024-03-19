from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from rest_framework import status,views, response
from rest_framework import authentication
from users.serializers import UserSerializer, AuthTokenSerializer, ClienteSerializer, PerfilSerializer, ClienteSerializerMatch
from users.models import User, Clientes
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateUserView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]
    
class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email2 = request.data.get('email', None)
        password2 = request.data.get('password', None)

        if not email2 or not password2:
            return response.Response({'message': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email2, password=password2)

        if not user:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '}, status=status.HTTP_404_NOT_FOUND)

        # Si el usuario ya tiene un token, lo usamos
        token = Token.objects.filter(user=user).first()

        if not token:
            # Si el usuario no tiene un token, creamos uno nuevo
            token = Token.objects.create(user=user)

        return response.Response({'token': token.key, 'cargo': user.cargo, 'id': user.id}, status=status.HTTP_200_OK)     

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):        
        request.email.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)
    
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
    
# ********************************** end point para perfil ************************************    
    
class ClientesPerfil(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        infoPerfil = Clientes.objects.all()
        serializer = PerfilSerializer(infoPerfil, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)          
    
# ********************************** end point para perfil ************************************    

# ********************************** end point que trae los del match ************************************    
    
class ClientesConMatchAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        clientes_con_match = Clientes.objects.filter(match='Si')
        serializer = ClienteSerializerMatch(clientes_con_match, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)          
    
# ********************************** end point que trae los del match ************************************     
    
    
    

class ClienteApiView(views.APIView):
    
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            user_Data = UserSerializer(data=request.data) 
            if user_Data.is_valid():
                user=user_Data.save()
            else:
                return response.Response(user_Data.errors, status=status.HTTP_400_BAD_REQUEST)  
        

            cliente_Data = request.data
            cliente_Data["id_User"] = user.id
            Cliente_Serializer = ClienteSerializer(data=cliente_Data)
            if Cliente_Serializer.is_valid():
                Cliente_Serializer.save()
                return response.Response(Cliente_Serializer.data, status=status.HTTP_200_OK)  
            else: 
                return response.Response(Cliente_Serializer.errors, status=status.HTTP_404_NOT_FOUND)  
        except Exception as e:
            print(e)
            return response.Response({"error":f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    




    


    
