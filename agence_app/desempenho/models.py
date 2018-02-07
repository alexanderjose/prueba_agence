# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaoAcompanhamentoSistema(models.Model):
    co_acompanhamento = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    co_sistema = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_acompanhamento_sistema'


class CaoAgendamento(models.Model):
    co_agendamento = models.BigAutoField(primary_key=True)
    dt_hr_inicio = models.DateTimeField()
    dt_hr_fim = models.DateTimeField(blank=True, null=True)
    co_status_agendamento = models.BigIntegerField()
    co_diary_report_consultor = models.BigIntegerField()
    co_complemento = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_agendamento'


class CaoArquiteturaOs(models.Model):
    co_arquitetura = models.BigIntegerField(primary_key=True)
    ds_arquitetura = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cao_arquitetura_os'


class CaoAtividade(models.Model):
    co_atividade = models.AutoField(primary_key=True)
    ds_atividade = models.CharField(max_length=30)
    co_tipo_usuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_atividade'


class CaoAtividadeConsultor(models.Model):
    co_atividade = models.AutoField(primary_key=True)
    ds_atividade = models.CharField(max_length=50)
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_atividade_consultor'


class CaoAtividadeReport(models.Model):
    co_cliente = models.IntegerField()
    inicio = models.CharField(max_length=30, blank=True, null=True)
    fim = models.CharField(max_length=30, blank=True, null=True)
    lembrete = models.CharField(max_length=50, blank=True, null=True)
    co_atividade = models.IntegerField()
    co_os = models.IntegerField()
    assunto = models.CharField(max_length=60, blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20)
    tempo = models.CharField(max_length=30, blank=True, null=True)
    co_usuario = models.CharField(max_length=50)
    data_ativ = models.DateTimeField()
    retorno = models.TextField()
    co_fase = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_atividade_report'


class CaoAtividadeTeste(models.Model):
    co_atividade = models.AutoField(primary_key=True)
    ds_atividade = models.CharField(max_length=30)
    co_tipo_usuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_atividade_teste'


class CaoAviso(models.Model):
    co_aviso = models.AutoField(primary_key=True)
    ds_aviso = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_aviso'


class CaoBancoDeHoras(models.Model):
    co_usuario = models.CharField(max_length=255)
    data_cadastro = models.DateField()
    segundos = models.IntegerField()
    tipo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cao_banco_de_horas'


class CaoBancoHoras(models.Model):
    co_banc_horas = models.AutoField(primary_key=True)
    co_usuario = models.CharField(max_length=20)
    periodo = models.CharField(max_length=7)
    min_mes = models.IntegerField()
    min_ferias = models.IntegerField()
    min_pago = models.IntegerField()
    min_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_banco_horas'


class CaoBoleto(models.Model):
    co_boleto = models.AutoField(primary_key=True)
    co_cliente = models.IntegerField()
    co_sistema = models.IntegerField()
    co_os = models.IntegerField()
    valor = models.CharField(max_length=128)
    vencimento = models.CharField(max_length=128)
    status = models.IntegerField()
    boleto = models.CharField(max_length=255, blank=True, null=True)
    linha_dig = models.CharField(max_length=255, blank=True, null=True)
    parcela = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_boleto'


class CaoBonus(models.Model):
    bon_categoria = models.IntegerField(primary_key=True)
    bon_inicio = models.IntegerField()
    bon_fim = models.IntegerField()
    bon_valor_sem = models.FloatField(blank=True, null=True)
    bon_valor_fimsem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_bonus'
        unique_together = (('bon_categoria', 'bon_inicio', 'bon_fim'),)


class CaoBonusStatus(models.Model):
    co_usuario = models.CharField(max_length=128)
    data_solic = models.DateField()
    mes = models.CharField(max_length=128)
    valor = models.CharField(max_length=128)
    is_solic = models.CharField(max_length=10, blank=True, null=True)
    is_pg = models.CharField(max_length=10, blank=True, null=True)
    is_horas = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_bonus_status'


class CaoCategoriasOmbudsman(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cao_categorias_ombudsman'


class CaoCidade(models.Model):
    co_cidade = models.BigAutoField(primary_key=True)
    no_cidade = models.CharField(max_length=30)
    co_uf = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_cidade'


class CaoCliente(models.Model):
    co_cliente = models.AutoField(primary_key=True)
    no_razao = models.CharField(max_length=50, blank=True, null=True)
    no_fantasia = models.CharField(max_length=50, blank=True, null=True)
    no_contato = models.CharField(max_length=30, blank=True, null=True)
    nu_telefone = models.CharField(max_length=15, blank=True, null=True)
    nu_ramal = models.CharField(max_length=6, blank=True, null=True)
    nu_cnpj = models.CharField(max_length=18, blank=True, null=True)
    ds_endereco = models.CharField(max_length=150, blank=True, null=True)
    nu_numero = models.IntegerField(blank=True, null=True)
    ds_complemento = models.CharField(max_length=150, blank=True, null=True)
    no_bairro = models.CharField(max_length=50)
    nu_cep = models.CharField(max_length=10, blank=True, null=True)
    no_pais = models.CharField(max_length=50, blank=True, null=True)
    co_ramo = models.BigIntegerField(blank=True, null=True)
    co_cidade = models.BigIntegerField()
    co_status = models.PositiveIntegerField(blank=True, null=True)
    ds_site = models.CharField(max_length=50, blank=True, null=True)
    ds_email = models.CharField(max_length=50, blank=True, null=True)
    ds_cargo_contato = models.CharField(max_length=50, blank=True, null=True)
    tp_cliente = models.CharField(max_length=2, blank=True, null=True)
    ds_referencia = models.CharField(max_length=100, blank=True, null=True)
    co_complemento_status = models.PositiveIntegerField(blank=True, null=True)
    nu_fax = models.CharField(max_length=15, blank=True, null=True)
    ddd2 = models.CharField(max_length=10, blank=True, null=True)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_cliente'


class CaoClienteContato(models.Model):
    co_cliente = models.PositiveIntegerField(primary_key=True)
    dt_contato = models.DateField(blank=True, null=True)
    fg_agendado = models.PositiveIntegerField(blank=True, null=True)
    hr_ini = models.TimeField(blank=True, null=True)
    hr_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_cliente_contato'


class CaoComissao(models.Model):
    co_comissao = models.AutoField(primary_key=True)
    co_fatura = models.IntegerField(unique=True)
    dt_efetuado = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_comissao'


class CaoComplemento(models.Model):
    co_complemento = models.BigAutoField(primary_key=True)
    ds_complemento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_complemento'


class CaoConhecimentoUsuario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    co_conhecimento = models.PositiveIntegerField()
    nv_conhecimento = models.PositiveIntegerField(blank=True, null=True)
    is_certificado = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_conhecimento_usuario'
        unique_together = (('co_usuario', 'co_conhecimento'),)


class CaoConhecimentos(models.Model):
    idconhecimento = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=100)
    conhecimento = models.TextField()
    url = models.TextField()
    tags = models.TextField()
    usuario = models.ForeignKey('CaoUsuario', models.DO_NOTHING, db_column='usuario')
    datahora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cao_conhecimentos'


class CaoConhecimentosFontes(models.Model):
    idfonte = models.AutoField(primary_key=True)
    idconhecimento = models.ForeignKey(CaoConhecimentos, models.DO_NOTHING, db_column='idconhecimento')
    datahora = models.DateTimeField()
    arquivo = models.CharField(max_length=50)
    caminho = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_conhecimentos_fontes'


class CaoCusto(models.Model):
    co_custo = models.BigAutoField(primary_key=True)
    co_tipo_custo = models.IntegerField()
    descricao = models.CharField(max_length=100)
    co_escritorio = models.IntegerField()
    dt_compra = models.DateField(blank=True, null=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    co_boleto = models.TextField(blank=True, null=True)
    valor = models.FloatField()
    parcela = models.CharField(max_length=5, blank=True, null=True)
    pag = models.IntegerField(blank=True, null=True)
    co_custo_high = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_custo'


class CaoDiaryReport(models.Model):
    co_diary_report = models.AutoField(primary_key=True)
    hr_gasta = models.TimeField(blank=True, null=True)
    co_atividade = models.IntegerField()
    ds_assunto = models.TextField()
    co_movimento = models.BigIntegerField()
    nu_os = models.BigIntegerField(blank=True, null=True)
    co_sistema = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_diary_report'


class CaoDiaryReportConsultor(models.Model):
    co_diary_report_consultor = models.AutoField(primary_key=True)
    co_movimento = models.IntegerField()
    co_atividade = models.IntegerField()
    ds_empresa = models.TextField()
    ds_assunto = models.TextField()
    dt_agendamento = models.DateTimeField()
    dt_agendamento_fim = models.DateTimeField(blank=True, null=True)
    vl_fechamento = models.FloatField()
    co_cliente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_diary_report_consultor'


class CaoDocumentacaoCasosUso(models.Model):
    nome = models.CharField(max_length=70)
    co_sistema = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_documentacao_casos_uso'


class CaoDocumentacaoOutros(models.Model):
    nome = models.CharField(max_length=70)
    co_sistema = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_documentacao_outros'


class CaoDocumentacaoSistema(models.Model):
    co_sistema = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    pasta = models.CharField(max_length=30)
    sub_grupo = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=60)
    dt_doc = models.DateTimeField()
    arquivo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cao_documentacao_sistema'


class CaoDrAtivComp(models.Model):
    id_ativ_comp = models.AutoField(primary_key=True)
    co_usuario = models.CharField(max_length=20)
    data = models.DateField()
    assunto = models.TextField()
    tempo_gasto = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cao_dr_ativ_comp'


class CaoEscalaRanking(models.Model):
    idescala = models.AutoField(primary_key=True)
    qtd_visual = models.IntegerField()
    pontuacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_escala_ranking'


class CaoEscritorio(models.Model):
    co_escritorio = models.AutoField(primary_key=True)
    local = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cao_escritorio'


class CaoFatura(models.Model):
    co_fatura = models.AutoField(primary_key=True)
    co_cliente = models.IntegerField()
    co_sistema = models.IntegerField()
    co_os = models.IntegerField()
    num_nf = models.IntegerField()
    total = models.FloatField()
    valor = models.FloatField()
    data_emissao = models.DateField()
    corpo_nf = models.TextField()
    comissao_cn = models.FloatField()
    total_imp_inc = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_fatura'


class CaoFaturaPag(models.Model):
    id_fatura_pag = models.AutoField(primary_key=True)
    co_fatura = models.IntegerField(unique=True)
    dt_efetuado = models.DateField()
    valor_pago = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_fatura_pag'


class CaoFeriados(models.Model):
    dia = models.PositiveIntegerField(blank=True, null=True)
    mes = models.PositiveIntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_feriados'


class CaoFormacaoIdiomaUsuario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    co_idioma = models.IntegerField()
    nv_leitura = models.IntegerField(blank=True, null=True)
    nv_escrita = models.IntegerField(blank=True, null=True)
    nv_fala = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_formacao_idioma_usuario'
        unique_together = (('co_usuario', 'co_idioma'),)


class CaoFormacaoUsuario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    tp_curso = models.CharField(max_length=13)
    ds_curso = models.CharField(max_length=50, blank=True, null=True)
    ds_instituicao = models.CharField(max_length=50, blank=True, null=True)
    dt_conclusao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_formacao_usuario'
        unique_together = (('co_usuario', 'tp_curso'),)


class CaoHelpAutor(models.Model):
    co_autor = models.AutoField(primary_key=True)
    no_autor = models.CharField(max_length=80)
    co_filial = models.IntegerField()
    nu_ddd1 = models.CharField(max_length=4, blank=True, null=True)
    nu_tel1 = models.CharField(max_length=15, blank=True, null=True)
    nu_ramal1 = models.CharField(max_length=6, blank=True, null=True)
    nu_ddd2 = models.CharField(max_length=4, blank=True, null=True)
    nu_tel2 = models.CharField(max_length=15, blank=True, null=True)
    nu_ramal2 = models.CharField(max_length=6, blank=True, null=True)
    ds_email = models.CharField(max_length=50, blank=True, null=True)
    ds_funcao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cao_help_autor'


class CaoHelpChamado(models.Model):
    co_chamado = models.AutoField(primary_key=True)
    ds_chamado = models.TextField()
    ds_solucao = models.TextField(blank=True, null=True)
    co_status = models.IntegerField()
    co_motivo = models.IntegerField()
    co_tela = models.IntegerField()
    co_autor = models.IntegerField()
    co_filial = models.IntegerField()
    co_sistema = models.BigIntegerField()
    dt_chamado = models.DateField()
    dt_solucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_help_chamado'


class CaoHelpFilial(models.Model):
    co_filial = models.AutoField(primary_key=True)
    no_filial = models.CharField(max_length=70)
    co_cliente = models.IntegerField()
    estado = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cao_help_filial'


class CaoHelpMotivoChamado(models.Model):
    co_motivo = models.AutoField(primary_key=True)
    ds_motivo = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'cao_help_motivo_chamado'


class CaoHelpStatusChamado(models.Model):
    co_status = models.AutoField(primary_key=True)
    ds_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_help_status_chamado'


class CaoHelpTelaChamado(models.Model):
    co_tela = models.AutoField(primary_key=True)
    co_cliente = models.IntegerField()
    co_sistema = models.IntegerField()
    ds_tela = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cao_help_tela_chamado'


class CaoHistOcorrenciasOs(models.Model):
    idocorrencia = models.AutoField(primary_key=True)
    co_os = models.ForeignKey('CaoOs', models.DO_NOTHING, db_column='co_os', blank=True, null=True)
    co_usuario = models.ForeignKey('CaoUsuario', models.DO_NOTHING, db_column='co_usuario', blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=7)
    descricao = models.TextField()
    responsavel = models.CharField(max_length=50)
    data_fechamento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_hist_ocorrencias_os'


class CaoHorarioAlmoco(models.Model):
    co_usuario = models.CharField(max_length=255)
    almoco_saida_hora = models.CharField(max_length=128)
    almoco_volta_hora = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cao_horario_almoco'


class CaoLogChamado(models.Model):
    co_chamado = models.IntegerField()
    dt_chamado = models.DateTimeField()
    co_usuario = models.CharField(max_length=128)
    co_daily = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_log_chamado'


class CaoMenu(models.Model):
    co_menu = models.AutoField(primary_key=True)
    ds_menu = models.CharField(max_length=255)
    ds_pagina = models.CharField(max_length=255)
    ds_imagem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_menu'


class CaoMenuContador(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    co_menu = models.PositiveIntegerField()
    nu_pontos = models.IntegerField()
    in_processado = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_menu_contador'
        unique_together = (('co_usuario', 'co_menu'),)


class CaoMovimento(models.Model):
    co_movimento = models.BigAutoField(primary_key=True)
    co_usuario = models.CharField(max_length=50)
    dt_entrada = models.DateTimeField()
    dt_saida_almoco = models.DateTimeField()
    dt_volta_almoco = models.DateTimeField()
    dt_saida = models.DateTimeField()
    is_encerrado = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_movimento'


class CaoMovimentoJustificativa(models.Model):
    co_movimento_justificativa = models.BigAutoField(primary_key=True)
    co_movimento = models.BigIntegerField()
    nu_os = models.BigIntegerField()
    ds_justificativa = models.TextField()

    class Meta:
        managed = False
        db_table = 'cao_movimento_justificativa'


class CaoMovimentoOs(models.Model):
    co_movimento_os = models.AutoField(primary_key=True)
    nu_os = models.IntegerField()
    co_sistema = models.BigIntegerField()
    co_tipo_movimento = models.BigIntegerField(blank=True, null=True)
    nu_valor = models.BigIntegerField(blank=True, null=True)
    ds_valor = models.TextField(blank=True, null=True)
    usuario_obs = models.CharField(max_length=30, blank=True, null=True)
    dt_ini = models.DateTimeField(blank=True, null=True)
    dt_fim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_movimento_os'


class CaoNoticia(models.Model):
    co_noticia = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.CharField(max_length=255)
    co_usuario = models.CharField(max_length=60)
    dt_noticia = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cao_noticia'


class CaoObsCliente(models.Model):
    co_obs = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=250)
    co_cliente = models.PositiveIntegerField()
    co_usuario = models.CharField(max_length=30, blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_obs_cliente'


class CaoObsSistema(models.Model):
    co_obs = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    co_sistema = models.BigIntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=20, blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_obs_sistema'


class CaoOmbudsman(models.Model):
    idtipo = models.ForeignKey('CaoTipoOmbudsman', models.DO_NOTHING, db_column='idtipo')
    idcategoria = models.ForeignKey(CaoCategoriasOmbudsman, models.DO_NOTHING, db_column='idcategoria')
    data = models.DateTimeField()
    comentario = models.TextField()
    co_escritorio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_ombudsman'


class CaoOs(models.Model):
    co_os = models.AutoField(primary_key=True)
    nu_os = models.IntegerField(blank=True, null=True)
    co_sistema = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=50, blank=True, null=True)
    co_arquitetura = models.IntegerField(blank=True, null=True)
    ds_os = models.CharField(max_length=200, blank=True, null=True)
    ds_caracteristica = models.CharField(max_length=200, blank=True, null=True)
    ds_requisito = models.CharField(max_length=200, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    co_status = models.IntegerField(blank=True, null=True)
    diretoria_sol = models.CharField(max_length=50, blank=True, null=True)
    dt_sol = models.DateField(blank=True, null=True)
    nu_tel_sol = models.CharField(max_length=20, blank=True, null=True)
    ddd_tel_sol = models.CharField(max_length=5, blank=True, null=True)
    nu_tel_sol2 = models.CharField(max_length=20, blank=True, null=True)
    ddd_tel_sol2 = models.CharField(max_length=5, blank=True, null=True)
    usuario_sol = models.CharField(max_length=50, blank=True, null=True)
    dt_imp = models.DateField(blank=True, null=True)
    dt_garantia = models.DateField(blank=True, null=True)
    co_email = models.IntegerField(blank=True, null=True)
    co_os_prospect_rel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os'


class CaoOsAnalista(models.Model):
    co_analista = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_analista'


class CaoOsChamado(models.Model):
    co_chamado = models.AutoField(primary_key=True)
    co_sistema = models.IntegerField()
    co_os = models.IntegerField()
    ds_chamado = models.CharField(max_length=255)
    co_tipo = models.IntegerField()
    co_prioridade = models.IntegerField()
    co_item = models.IntegerField()
    descricao = models.TextField()
    ds_solucao = models.TextField()
    tempo = models.CharField(max_length=30)
    dt_chamado = models.DateTimeField()
    status = models.IntegerField()
    co_usuario = models.CharField(max_length=255)
    co_analista = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_chamado'


class CaoOsDailyReport(models.Model):
    co_daily = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_fase = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=50, blank=True, null=True)
    ds_assunto = models.TextField(blank=True, null=True)
    tempo_gasto = models.TimeField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    co_status_atual = models.IntegerField(blank=True, null=True)
    co_chamado = models.IntegerField(blank=True, null=True)
    co_atividade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_daily_report'


class CaoOsEmail(models.Model):
    co_email = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=255)
    co_cliente = models.IntegerField()
    ativo = models.IntegerField()
    ddd = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=40, blank=True, null=True)
    cargo = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_email'


class CaoOsFase(models.Model):
    co_fase = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    descricao_ingl = models.CharField(max_length=200)
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_fase'


class CaoOsItemMenu(models.Model):
    co_item = models.AutoField(primary_key=True)
    ds_item = models.CharField(max_length=255)
    co_sistema = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_os_item_menu'


class CaoOsObs(models.Model):
    co_obs = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=80, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_obs'


class CaoOsObsChamado(models.Model):
    co_obs = models.AutoField(primary_key=True)
    co_chamado = models.IntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=80, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    arquivo_obs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_obs_chamado'


class CaoOsPrazo(models.Model):
    co_prazo = models.AutoField(primary_key=True)
    co_os = models.IntegerField(blank=True, null=True)
    co_fase = models.PositiveIntegerField(blank=True, null=True)
    total_analista = models.IntegerField(blank=True, null=True)
    total_hora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_os_prazo'


class CaoOsStatus(models.Model):
    co_status_atual = models.AutoField(primary_key=True)
    ds_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_os_status'


class CaoPagamento(models.Model):
    co_pagamento = models.BigAutoField(primary_key=True)
    co_usuario = models.CharField(max_length=20)
    tp_pagamento = models.CharField(max_length=2)
    dt_pagamento = models.DateField()
    vl_pagamento = models.FloatField()
    dt_referencia_pagamento = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_pagamento'


class CaoParticipacaoFuncionario(models.Model):
    co_part_funcionario = models.AutoField(primary_key=True)
    pc_participacao = models.FloatField()
    co_usuario = models.CharField(max_length=20)
    co_escritorio = models.PositiveIntegerField()
    dt_referencia = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_participacao_funcionario'


class CaoPermissao(models.Model):
    co_usuario = models.ForeignKey('CaoUsuario', models.DO_NOTHING, db_column='co_usuario')
    permissao_intervalo = models.CharField(max_length=1)
    permissao_hora_extra = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cao_permissao'


class CaoPermissaoHoraExtra(models.Model):
    id_permissao = models.AutoField(primary_key=True)
    co_movimento = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_permissao_hora_extra'


class CaoPontosConhecimento(models.Model):
    idpontos = models.AutoField(primary_key=True)
    pontuacao = models.ForeignKey(CaoEscalaRanking, models.DO_NOTHING, db_column='pontuacao')
    co_coordenador = models.ForeignKey('CaoUsuario', models.DO_NOTHING, db_column='co_coordenador')
    idconhecimento = models.ForeignKey(CaoConhecimentos, models.DO_NOTHING, db_column='idconhecimento')

    class Meta:
        managed = False
        db_table = 'cao_pontos_conhecimento'


class CaoRamo(models.Model):
    co_ramo = models.BigAutoField(primary_key=True)
    ds_ramo = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cao_ramo'


class CaoRelEmailOs(models.Model):
    co_email = models.IntegerField()
    co_os = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cao_rel_email_os'


class CaoSalario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    dt_alteracao = models.DateField()
    brut_salario = models.FloatField()
    liq_salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cao_salario'
        unique_together = (('co_usuario', 'dt_alteracao'),)


class CaoSalarioPag(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    co_usuario = models.ForeignKey('CaoUsuario', models.DO_NOTHING, db_column='co_usuario')
    dt_efetuado = models.DateField()
    status = models.CharField(max_length=10)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_salario_pag'
        unique_together = (('co_usuario', 'dt_efetuado'),)


class CaoServico(models.Model):
    co_servico = models.AutoField(primary_key=True)
    ds_servico = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_servico'


class CaoSistema(models.Model):
    co_sistema = models.AutoField(primary_key=True)
    co_cliente = models.PositiveIntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=50, blank=True, null=True)
    co_arquitetura = models.PositiveIntegerField(blank=True, null=True)
    no_sistema = models.CharField(max_length=200, blank=True, null=True)
    ds_sistema_resumo = models.TextField(blank=True, null=True)
    ds_caracteristica = models.TextField(blank=True, null=True)
    ds_requisito = models.TextField(blank=True, null=True)
    no_diretoria_solic = models.CharField(max_length=100, blank=True, null=True)
    ddd_telefone_solic = models.CharField(max_length=5, blank=True, null=True)
    nu_telefone_solic = models.CharField(max_length=20, blank=True, null=True)
    no_usuario_solic = models.CharField(max_length=100, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)
    dt_entrega = models.DateField(blank=True, null=True)
    co_email = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_sistema'


class CaoSistemaObs(models.Model):
    co_obs = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    co_sistema = models.BigIntegerField(blank=True, null=True)
    co_usuario = models.CharField(max_length=20, blank=True, null=True)
    dt_obs = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_sistema_obs'


class CaoStatusAgendamento(models.Model):
    co_status_agendamento = models.BigAutoField(primary_key=True)
    ds_status_agendamento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cao_status_agendamento'


class CaoStatusCliente(models.Model):
    co_status = models.AutoField(primary_key=True)
    ds_status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cao_status_cliente'


class CaoStatusClienteComplemento(models.Model):
    co_complemento_status = models.AutoField(primary_key=True)
    ds_status = models.CharField(max_length=50, blank=True, null=True)
    co_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_status_cliente_complemento'


class CaoStatusOs(models.Model):
    co_status_atual = models.AutoField(primary_key=True)
    ds_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_status_os'


class CaoTempImport(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cao_temp_import'


class CaoTipoConhecimentoUsuario(models.Model):
    co_conhecimento = models.AutoField(primary_key=True)
    ds_conhecimento = models.CharField(max_length=20, blank=True, null=True)
    co_sistema = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cao_tipo_conhecimento_usuario'


class CaoTipoCusto(models.Model):
    co_tipo_custo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cao_tipo_custo'


class CaoTipoIdiomaUsuario(models.Model):
    co_idioma = models.AutoField(primary_key=True)
    ds_idioma = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_tipo_idioma_usuario'


class CaoTipoOmbudsman(models.Model):
    idtipo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cao_tipo_ombudsman'


class CaoTipoSistemaUsuario(models.Model):
    co_sistema = models.AutoField(primary_key=True)
    ds_sistema = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_tipo_sistema_usuario'


class CaoUf(models.Model):
    co_uf = models.BigAutoField(primary_key=True)
    ds_uf = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'cao_uf'


class CaoUsuario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    no_usuario = models.CharField(max_length=50)
    ds_senha = models.CharField(max_length=14)
    co_usuario_autorizacao = models.CharField(max_length=20, blank=True, null=True)
    nu_matricula = models.BigIntegerField(blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    dt_admissao_empresa = models.DateField(blank=True, null=True)
    dt_desligamento = models.DateField(blank=True, null=True)
    dt_inclusao = models.DateTimeField(blank=True, null=True)
    dt_expiracao = models.DateField(blank=True, null=True)
    nu_cpf = models.CharField(max_length=14, blank=True, null=True)
    nu_rg = models.CharField(max_length=20, blank=True, null=True)
    no_orgao_emissor = models.CharField(max_length=10, blank=True, null=True)
    uf_orgao_emissor = models.CharField(max_length=2, blank=True, null=True)
    ds_endereco = models.CharField(max_length=150, blank=True, null=True)
    no_email = models.CharField(max_length=100, blank=True, null=True)
    no_email_pessoal = models.CharField(max_length=100, blank=True, null=True)
    nu_telefone = models.CharField(max_length=64, blank=True, null=True)
    dt_alteracao = models.DateTimeField()
    url_foto = models.CharField(max_length=255, blank=True, null=True)
    instant_messenger = models.CharField(max_length=80, blank=True, null=True)
    icq = models.PositiveIntegerField(blank=True, null=True)
    msn = models.CharField(max_length=50, blank=True, null=True)
    yms = models.CharField(max_length=50, blank=True, null=True)
    ds_comp_end = models.CharField(max_length=50, blank=True, null=True)
    ds_bairro = models.CharField(max_length=30, blank=True, null=True)
    nu_cep = models.CharField(max_length=10, blank=True, null=True)
    no_cidade = models.CharField(max_length=50, blank=True, null=True)
    uf_cidade = models.CharField(max_length=2, blank=True, null=True)
    dt_expedicao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cao_usuario'


class CaoUsuarioDtDisp(models.Model):
    co_dt_disp = models.AutoField(primary_key=True)
    co_usuario = models.CharField(max_length=20, blank=True, null=True)
    dt_disp = models.DateField()
    dt_alt = models.DateField()

    class Meta:
        managed = False
        db_table = 'cao_usuario_dt_disp'


class CaoValorDescanso(models.Model):
    co_usuario = models.CharField(max_length=40)
    segundos = models.CharField(max_length=50)
    mes_referencia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cao_valor_descanso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PermissaoSistema(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20)
    co_tipo_usuario = models.BigIntegerField()
    co_sistema = models.BigIntegerField()
    in_ativo = models.CharField(max_length=1)
    co_usuario_atualizacao = models.CharField(max_length=20, blank=True, null=True)
    dt_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permissao_sistema'
        unique_together = (('co_usuario', 'co_tipo_usuario', 'co_sistema'),)


class TipoUsuario(models.Model):
    co_tipo_usuario = models.BigIntegerField(primary_key=True)
    ds_tipo_usuario = models.CharField(max_length=32)
    co_sistema = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
        unique_together = (('co_tipo_usuario', 'co_sistema'),)
