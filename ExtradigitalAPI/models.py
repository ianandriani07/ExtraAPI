import json


from django.db import models

# Modelos dos campos da tabela Ecfgusuario


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
    # cdpessoa = models.ForeignKey('Ecdtpessoa', models.DO_NOTHING, db_column='cdpessoa', blank=True, null=True)
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

# Classe de usuarios apenas com os campos delogin, nmusuario e desenha


class Usuarios(models.Model):
    delogin = models.CharField(primary_key=True, max_length=20)
    nmusuario = models.CharField(max_length=80)
    desenha = models.CharField(max_length=32, blank=True, null=True)
    flativo = models.CharField(max_length=1, blank=True, null=True)
    imthumb = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecfgusuario'  # Definindo a tabela aonde os dados serão armazenados


class Vcdtfilalogmein(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    customfield0 = models.CharField(db_column='CustomField0', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customfield1 = models.TextField(db_column='CustomField1', blank=True, null=True)  # Field name made lowercase.
    customfield2 = models.CharField(db_column='CustomField2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customfield3 = models.CharField(db_column='CustomField3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customfield4 = models.CharField(db_column='CustomField4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customfield5 = models.CharField(db_column='CustomField5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    technician = models.CharField(db_column='Technician', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cdcartorio = models.IntegerField(db_column='CDCARTORIO', blank=True, null=True)  # Field name made lowercase.
    nmpessoa = models.CharField(db_column='NMPESSOA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    desituacaoimplantacao = models.CharField(db_column='deSituacaoImplantacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imthumb = models.BinaryField(db_column='IMTHUMB', blank=True, null=True)  # Field name made lowercase.
    flbeep = models.CharField(db_column='FLBEEP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VCDTFILALOGMEIN'


class Ecdtlogmein(models.Model):

    cdlogmein = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    status = models.CharField(max_length=50, blank=True, null=True)
    entryid = models.IntegerField(blank=True, null=True)
    entry = models.CharField(max_length=50, blank=True, null=True)
    technicianid = models.IntegerField(blank=True, null=True)
    technician = models.CharField(max_length=30, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    waitingtime = models.DateTimeField(blank=True, null=True)
    customfield0 = models.CharField(max_length=20, blank=True, null=True)
    customfield1 = models.TextField(blank=True, null=True)
    customfield2 = models.CharField(max_length=50, blank=True, null=True)
    customfield3 = models.CharField(max_length=30, blank=True, null=True)
    customfield4 = models.CharField(max_length=30, blank=True, null=True)
    customfield5 = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    transferredto = models.CharField(max_length=30, blank=True, null=True)
    transferredcomment = models.CharField(max_length=100, blank=True, null=True)
    isleadtechnician = models.CharField(max_length=10, blank=True, null=True)
    handingoff = models.CharField(max_length=10, blank=True, null=True)
    nuprioridade = models.IntegerField(blank=True, null=True)
    flbeep = models.CharField(max_length=10, blank=True, null=True)
    teste = models.IntegerField(blank=True, null=True)
    deresposta1 = models.CharField(max_length=2000, blank=True, null=True)
    deresposta2 = models.CharField(max_length=2000, blank=True, null=True)
    deresposta3 = models.CharField(max_length=2000, blank=True, null=True)
    depesquisaemitidapelotecnico = models.CharField(max_length=10, blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    lastdatestatus = models.DateTimeField(blank=True, null=True)
    flprocessado = models.CharField(max_length=1, blank=True, null=True)

    @classmethod
    def sacGetTMA(self):
        dados = Ecdtlogmein.objects.raw(
            'SELECT ' +
            '-1 as cdlogmein, '
            '  cast(CAST(AVG(CAST(CAST(cast(EndTime as datetime) - (cast(StartTime as datetime) + cast(WaitingTime as datetime)) AS DATETIME) AS DECIMAL(10,5))) AS datetime) as time) as TMA ' +
            'from ' +
            '  ecdtlogmein ' +
            'where ' +
            '  cast(StartTime as date) = cast(dbo.cdGetDate() as date) and ' +
            'status <> \'Waiting\' and EndTime is not null')

        return dados

    @classmethod
    def sacGetTME(cls):
        c_SQL = Ecdtlogmein.objects.raw(
            'select ' +
            '-1 as cdlogmein, ' +
            '  cast(CAST(AVG(CAST(cast(WaitingTime as datetime) AS DECIMAL(10,5))) AS datetime) as time) as TME ' +
            'from ' +
            '  ECDTLOGMEIN ' +
            'where ' +
            '  cast(convert(datetime, StartTime) as date) = cast(convert(datetime, dbo.cdGetDate()) as date) and ' +
            ' WaitingTime is not null')

        return c_SQL

    @classmethod
    def sacGetPERDAS(cls):
        c_SQL = Ecdtlogmein.objects.raw(
            'select ' +
            '-1 as cdlogmein, '
            ' count(cdlogmein) as conta ' +
            'from ' +
            '  ecdtlogmein ' +
            'where ' +
            '  cast(starttime as date) = cast(dbo.cdGetDate() as date) and ' +
            '  (Technician = \'\' or Technician is null) and Status <> \'Waiting\' and Status <> \'Closed by active customer\'')

        return c_SQL

    @classmethod
    def sacGetAGUARDANDO(cls):

        dados = Ecdtlogmein.objects.raw(
            'select ' +
            '-1 as cdlogmein, '
            '  count(L.CDLOGMEIN) as id ' +
            'from ' +
            '  ECDTLOGMEIN L ' +
            'where ' +
            '  convert(date, L.StartTime) = convert(date, dbo.cdGetDate()) and (L.Status = \'Waiting\' ) ')

        return dados

    @classmethod
    def sacGetEM_ATENDIMENTO(cls):
        c_SQL = Ecdtlogmein.objects.raw(
            'select ' +
            '-1 as cdlogmein, '
            '  count(CDLOGMEIN) as conta ' +
            'from ' +
            '  ECDTLOGMEIN L left outer join ' +
            '  ECDTCARTORIOS C ON C.cdCartorio = L.cdCartorio left outer join ' +
            '  ECDTPESSOA P ON P.cdPessoa = C.cdCartorioPessoa left outer join ' +
            '  ECDTCIDADE CI ON CI.sgUF = P.sgUF and CI.cdCidade = P.cdCidade ' +
            'where ' +
            '  convert(date, StartTime) = convert(date, dbo.cdGetDate()) and Status = \'Active\' ')

        return c_SQL

    class Meta:
        managed = False
        db_table = 'ecdtlogmein'
