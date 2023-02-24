from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuarios, Vcdtfilalogmein, Ecdtlogmein

# Criando serialização de Login


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios  # Utilizando o model Usuarios como base
        fields = ('delogin', 'nmusuario')  # Definindo os campos que serão serializados

# Criando serialização de Registro


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios  # Utilizando o model Usuarios como base
        fields = ('delogin', 'nmusuario', 'desenha', 'flativo')  # Definindo campos que serão serializados
        extra_kwargs = {'desenha': {'write_only': True}}  # Definindo senha como apenas escrever, para que não seja
                                                          # possivel visualizar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class VcdtfilalogmeinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vcdtfilalogmein
        fields = '__all__'

        def sacPegaListaDeAtendimentos(self):
            Vcdtfilalogmein.objects.all()


class EcdtfilalogmeinSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ecdtlogmein
        fields = '__all__'
