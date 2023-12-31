# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ecfgusuario(models.Model):
    delogin = models.CharField(primary_key=True, max_length=20)
    nmusuario = models.CharField(max_length=50)
    flativo = models.CharField(max_length=1, blank=True, null=True)
    desenha = models.CharField(max_length=32, blank=True, null=True)
    desuperusuario = models.CharField(max_length=32, blank=True, null=True)
    deemail = models.CharField(max_length=50, blank=True, null=True)
    nuusuario = models.IntegerField(blank=True, null=True)
    defuncao = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    numatricula = models.CharField(max_length=20, blank=True, null=True)
    flbiologin = models.CharField(max_length=1, blank=True, null=True)
    imusuario = models.BinaryField(blank=True, null=True)
    flpodeatualizar = models.CharField(max_length=1, blank=True, null=True)
    flpodetrocarsituacao = models.CharField(max_length=1, blank=True, null=True)
    flpodeconcluirativ = models.CharField(max_length=1, blank=True, null=True)
    mmconfiguracoes = models.TextField(blank=True, null=True)
    flnovolayout = models.CharField(max_length=1, blank=True, null=True)
    flcronograma = models.CharField(max_length=1, blank=True, null=True)
    nmlogmein = models.CharField(max_length=30, blank=True, null=True)
    deemaillogmein = models.CharField(max_length=100, blank=True, null=True)
    cdpessoa = models.ForeignKey('Ecdtpessoa', models.DO_NOTHING, db_column='cdpessoa', blank=True, null=True)
    imthumb = models.BinaryField(blank=True, null=True)
    dtentrada = models.DateField(blank=True, null=True)
    dtsaida = models.DateField(blank=True, null=True)
    flmobile = models.CharField(max_length=1, blank=True, null=True)
    dedeviceid = models.CharField(max_length=255, blank=True, null=True)
    dedevicetoken = models.CharField(max_length=255, blank=True, null=True)
    depin = models.CharField(max_length=32, blank=True, null=True)
    dtultimologin = models.DateTimeField(blank=True, null=True)
    deultimoip = models.CharField(max_length=32, blank=True, null=True)
    deultimohost = models.CharField(max_length=64, blank=True, null=True)
    nuversaosac = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecfgusuario'
