import knox.auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authentication import get_authorization_header

import base64
import json

from django.core import serializers
from .models import Usuarios, Vcdtfilalogmein, Ecdtlogmein
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer, VcdtfilalogmeinSerializer, LoginSerializer, \
    EcdtfilalogmeinSerilizer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Registrando um novo usuário na base de dados e no DjangoAdmin
class RegisterAPI(generics.GenericAPIView):  # Usando um View genérica
    serializer_class = RegisterSerializer  # Atribuindo a serializer_class ao RegisterSerializer para serializar as mode
    permission_classes = (permissions.IsAdminUser,)

    # Definindo método POST
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Pegando os dados do POST e serializando eles
        serializer.is_valid(raise_exception=True)  # Verificando se os dados serializados são válidos, caso não seja,
        # envia uma mensagem de erro
        usuario = serializer.save(flativo='S')  # Fazendo INSERT do usuário no banco de dados
        user = User.objects.create_user(usuario.delogin, None, usuario.desenha)  # Com os dados inseridos no banco de
        # dados, é criado um novo Usuário no
        # Django admin
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados serializados e o status de
        # criado


# Login de usuários


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)  # Configurando permissões para que qualquer pessoa possa logar

    # Definindo o método POST para o usuário inserir dados

    def post(self, request, format=None):
        delogin = request.data['username']  # Criando váriavel delogin para armezenar as informações deserializadas do
        # usuário no método POST
        desenha = request.data['password']  # Criando váriavel desenha para armezenar as informações deserializadas de
        # senha no método POST
        serializer = AuthTokenSerializer(data=request.data)  # Serializando os dados para o AuthTokenSerializer

        # Verificando se o serializer não foi valido
        if serializer.is_valid() == False:
            # Caso o serializer não sejá valido, sera feito um get no banco de dados, para verificar se os dados
            # passados no método POST já estão inseridas na tabela
            pesquisa = (Usuarios.objects.get(delogin=delogin, desenha=desenha, flativo='S'))

            # Verficando se os dados do banco de dados são iguais aos inseridos no métodos post
            if (delogin == pesquisa.delogin) and (desenha == desenha) and (pesquisa.flativo == 'S'):
                # Caso os dados sejam iguais, será criado um usuário novo no Django com essas informações
                user = User.objects.create_user(delogin, None, desenha)  # Criando usuário...
                autorizado = True
            else:
                return Response('Usuario invalido')  # Caso os dados não sejam iguais o usuário é invalido
        else:
            autorizado = True
            user = serializer.validated_data['user']

        if autorizado is True:

            pesquisa_flativo = (Usuarios.objects.get(delogin=delogin, flativo='S'))

            if pesquisa_flativo.flativo == 'S':

                login(request, user)
                return super(LoginAPI, self).post(request, format=None)
                # Retorna o tempo de expiração do token e o token associado ao usuário
            else:
                return Response('Seu usuário não está ativo.')

        else:
            return Response('Não autorizado')


class SacPegaImagem(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    # serializer_class = UserSerializer

    def get(self, request):
        user = request.user.username
        pesquisa = Usuarios.objects.get(delogin=user)
        nome = pesquisa.nmusuario
        img = pesquisa.imthumb

        data = {
            "nome": nome
        }

        if img is not None:
            b64 = base64.b64encode(img)
            data.update({"img": b64})

        return Response(data)


class sacPegaFilaDeAtendimento(generics.ListAPIView):
    queryset = Vcdtfilalogmein.objects.all()
    serializer_class = VcdtfilalogmeinSerializer


class sacPegaDadosDoPainelDeAtendimentos(generics.RetrieveAPIView):

    def get(self, request):
        pesq_TMA = Ecdtlogmein.sacGetTMA()[0]
        pesq_TME = Ecdtlogmein.sacGetTME()[0]
        pesq_aguard = Ecdtlogmein.sacGetAGUARDANDO()[0]
        pesq_perdas = Ecdtlogmein.sacGetPERDAS()[0]
        pesq_em_atend = Ecdtlogmein.sacGetEM_ATENDIMENTO()[0]

        fila_logmein = Vcdtfilalogmein.objects.all()

        camp_pesq_tma = pesq_TMA.TMA
        camp_pesq_tme = pesq_TME.TME
        camp_pesq_aguard = pesq_aguard.cdlogmein
        camp_pesq_perdas = pesq_perdas.conta
        camp_pesq_em_atend = pesq_em_atend.conta

        data = {"TMA": camp_pesq_tma}
        data.update({"TME": camp_pesq_tme})
        data.update({"id": camp_pesq_aguard})
        data.update({"Perdas": camp_pesq_perdas})
        data.update({"Em atendimento": camp_pesq_em_atend})

        serializer = VcdtfilalogmeinSerializer(fila_logmein, many=True)

        return Response((data, serializer.data))
