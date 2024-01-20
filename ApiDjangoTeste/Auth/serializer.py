from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_active', 'date_joined', 'type')
    extra_kwargs = {
      'password': {'write_only': True}
    }

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicionar informações do usuário ao payload do token, se desejado
        # token['email'] = user.email
        # token['id'] = str(user.id)
        # token['role'] = user.role
        
        return token
    
    
    def validate(self, attrs):
        data = super().validate(attrs)

        # Serializa os dados do usuário/ adicionando o objeto do usuário serializado à resposta da API. Isso significa que, além do token JWT, a resposta da API também incluirá os dados do usuário como um objeto separado.
        user_serializer = UserSerializer(self.user).data
        print(user_serializer)
        data.update({'user': user_serializer})
        
        return data