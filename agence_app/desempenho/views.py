from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
from .models import (
    CaoUsuario, PermissaoSistema, CaoFatura, CaoOs, CaoSalario
)
from django.db.models.functions import(
    ExtractMonth, ExtractYear
)
from django.db.models import Sum, F, Max, Min, Count
from datetime import datetime
import json


class DesempenhoHomeView(TemplateView):
    template_name = 'desempenho/home.html'

    # def dispatch(self, request, *args, **kwargs):
    #     user = self.request.user
    #     if user.is_anonymous():
    #         return super(DesempenhoHomeView, self).dispatch(
    #             request, *args, **kwargs)
    #
    #     return super(DesempenhoHomeView, self).dispatch(
    #         request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DesempenhoHomeView, self).get_context_data(**kwargs)

        # Seteando las fechas limites donde hay facturas disponibles (para los
        # campos de fecha)
        max_year = CaoFatura.objects.all().aggregate(
            Max('data_emissao'))['data_emissao__max'].strftime('%d-%m-%Y')
        min_year = CaoFatura.objects.all().aggregate(
            Min('data_emissao'))['data_emissao__min'].strftime('%d-%m-%Y')

        # Condiciones iniciales: Usuarios disponibles para generar consultas en
        # las tablas de ganancias
        permissao_sistema = PermissaoSistema.objects.filter(
            co_sistema=1, in_ativo='S', co_tipo_usuario__in=[0, 1, 2]
        ).values('co_usuario')
        consultores = CaoUsuario.objects.filter(
            co_usuario__in=permissao_sistema
        ).values('co_usuario', 'no_usuario')

        context['max_year'] = max_year
        context['min_year'] = min_year
        context['consultores'] = consultores
        return context


def detail_receitas(request):
    consultores = request.GET.getlist('consultores[]', None)
    fecha_ini = request.GET.get('fecha_ini', None)
    fecha_fin = request.GET.get('fecha_fin', None)
    fecha_ini_object = datetime.strptime(fecha_ini, '%d-%m-%Y')
    fecha_fin_object = datetime.strptime(fecha_fin, '%d-%m-%Y')
    data = {}
    items = []
    for consultor in consultores:
        consultor_nombre_object = CaoUsuario.objects.filter(
            co_usuario=consultor
        ).values('no_usuario')
        for cno in consultor_nombre_object:
            consultor_nombre = cno.get('no_usuario')
        orden_servicio = CaoOs.objects.filter(
            co_usuario=consultor
        ).values('co_os')
        # Query para costo fijo
        costo_fijo = CaoSalario.objects.filter(
            co_usuario=consultor
        ).values('brut_salario')
        for cf in costo_fijo:
            salario = cf.get('brut_salario')
        # Query para Receita Liquida
        receita_liquida = CaoFatura.objects.filter(
            co_os__in=orden_servicio,
            data_emissao__year__gte=fecha_ini_object.year,
            data_emissao__month__gte=fecha_ini_object.month,
            data_emissao__year__lte=fecha_fin_object.year,
            data_emissao__month__lte=fecha_fin_object.month
        ).annotate(
            month=ExtractMonth('data_emissao'),
            year=ExtractYear('data_emissao')
        ).values('year', 'month').annotate(
            rl=(Sum(F('valor') - (F('valor') * (F('total_imp_inc') / 100))))
        ).values('rl', 'month', 'year').annotate(
            vc=(F('rl')) * (F('comissao_cn') / 100)
        ).order_by('month')

        month_temp = 1
        year_temp = 0
        rl_acum = 0
        vc_acum = 0
        rl_totales = 0
        vc_totales = 0
        cf_totales = 0
        to_totales = 0
        data_table = []
        total_row = []
        data_row = {}
        totales = {}
        for receta in receita_liquida:
            ganancias = {}
            if receta.get('year') == year_temp:
                if receta.get('month') == month_temp:
                    rl_acum = rl_acum + receta.get('rl')
                    vc_acum = vc_acum + receta.get('vc')
                else:
                    month_temp = receta.get('month')
                    if month_temp != 0:
                        # print(round(rl_acum, 2))
                        ganancias['month'] = receta.get('month')
                        ganancias['year'] = receta.get('year')
                        ganancias['ganancias'] = round(rl_acum, 2)
                        rl_totales = rl_totales + round(rl_acum, 2)
                        ganancias['comision'] = round(vc_acum, 2)
                        vc_totales = vc_totales + round(vc_acum, 2)
                        ganancias['total'] =\
                            round(rl_acum - (salario + vc_acum), 2)
                        to_totales = to_totales +\
                            round((rl_acum - (salario + vc_acum)), 2)
                        data_table.append(ganancias)
                        ganancias['costo_fijo'] = salario
                        cf_totales = cf_totales + salario
                    rl_acum = 0
                    vc_acum = 0
                    rl_acum = rl_acum + receta.get('rl')
                    vc_acum = vc_acum + receta.get('vc')
            else:
                year_temp = receta.get('year')
                if receta.get('month') == month_temp:
                    rl_acum = rl_acum + receta.get('rl')
                    vc_acum = vc_acum + receta.get('vc')
                else:
                    month_temp = receta.get('month')
                    # print('MES AUX: ' + str(month_temp))
                    if month_temp != 0:
                        # print(round(rl_acum, 2))
                        ganancias['month'] = receta.get('month')
                        ganancias['year'] = receta.get('year')
                        ganancias['ganancias'] = round(rl_acum, 2)
                        rl_totales = rl_totales + round(rl_acum, 2)
                        ganancias['comision'] = round(vc_acum, 2)
                        vc_totales = vc_totales + round(vc_acum, 2)
                        ganancias['total'] =\
                            round(rl_acum - (salario + vc_acum), 2)
                        to_totales = to_totales +\
                            round((rl_acum - (salario + vc_acum)), 2)
                        data_table.append(ganancias)
                        ganancias['costo_fijo'] = salario
                        cf_totales = cf_totales + salario
                    rl_acum = 0
                    vc_acum = 0
                    rl_acum = rl_acum + receta.get('rl')
                    vc_acum = vc_acum + receta.get('vc')
        totales['rl_totales'] = round(rl_totales, 2)
        totales['vc_totales'] = round(vc_totales, 2)
        totales['cf_totales'] = round(cf_totales, 2)
        totales['to_totales'] = round(to_totales, 2)
        total_row.append(totales)
        data_row['consultor'] = consultor_nombre
        data_row['data'] = data_table
        data_row['totales'] = total_row
        data_table = []
        total_row = []
        items.append(data_row)
        data['items'] = items
        # print(data)
    return render(request, 'desempenho/recetas.html', data)


def ganancias_liquidas(orden_servicio, fecha_inicio, fecha_fin):
    ganancias = CaoFatura.objects.filter(
        co_os__in=orden_servicio,
        data_emissao__year__gte=fecha_inicio.year,
        data_emissao__month__gte=fecha_inicio.month,
        data_emissao__year__lte=fecha_fin.year,
        data_emissao__month__lte=fecha_fin.month
    ).annotate(
        month=ExtractMonth('data_emissao'),
        year=ExtractYear('data_emissao')
    ).values('year', 'month').annotate(
        rl=(Sum(F('valor') - (F('valor') * (F('total_imp_inc') / 100))))
    ).order_by('month')
    return ganancias


def detail_pizza(request):
    consultores = request.GET.getlist('consultores[]', None)
    fecha_ini = request.GET.get('fecha_ini', None)
    fecha_fin = request.GET.get('fecha_fin', None)
    fecha_ini_object = datetime.strptime(fecha_ini, '%d-%m-%Y')
    fecha_fin_object = datetime.strptime(fecha_fin, '%d-%m-%Y')
    data = {}
    data_pizza = {}
    data_consultor = []
    for consultor in consultores:
        consultor_nombre_object = CaoUsuario.objects.filter(
            co_usuario=consultor
        ).values('no_usuario')
        for cno in consultor_nombre_object:
            consultor_nombre = cno.get('no_usuario')
        total_ganancia_consultor = 0
        orden_servicio = CaoOs.objects.filter(
            co_usuario=consultor
        ).values('co_os')

        # Ganancia Liquida
        ganancias = ganancias_liquidas(
            orden_servicio,
            fecha_ini_object,
            fecha_fin_object
        )
        for ganancia in ganancias:
            total_ganancia_consultor =\
                total_ganancia_consultor + ganancia.get('rl')
        # Suma de todas las ganancias individuales de los consultores
        # total_ganancia = total_ganancia + total_ganancia_consultor
        # if round(total_ganancia_consultor, 2) > 0:
        data_consultor.append(consultor_nombre)
        data_consultor.append(round(total_ganancia_consultor, 2))
        data_pizza[consultor_nombre] = data_consultor
        data_consultor = []
    data['json_to_pizza'] = json.dumps(data_pizza)
    return render(request, 'desempenho/pizza.html', data)


def detail_bar(request):
    consultores = request.GET.getlist('consultores[]', None)
    fecha_ini = request.GET.get('fecha_ini', None)
    fecha_fin = request.GET.get('fecha_fin', None)
    fecha_ini_object = datetime.strptime(fecha_ini, '%d-%m-%Y')
    fecha_fin_object = datetime.strptime(fecha_fin, '%d-%m-%Y')
    data_bar = {}
    costo_fijo_total = 0
    lista_bar = []
    cantidad_consultores = 0
    data = {}
    for consultor in consultores:
        consultor_nombre_object = CaoUsuario.objects.filter(
            co_usuario=consultor
        ).values('no_usuario')
        for cno in consultor_nombre_object:
            consultor_nombre = cno.get('no_usuario')
        total_ganancia = 0
        # Todas las facuras (Ordenes de servicio) generadas por el consultor
        orden_servicio = CaoOs.objects.filter(
            co_usuario=consultor
        ).values('co_os')

        # Todas las facturas generadas por el consultor sin el calculo de
        # impuesto respectivo en un periodo determinado de tiempo
        ganancias = ganancias_liquidas(
            orden_servicio,
            fecha_ini_object,
            fecha_fin_object
        )
        # Ganancia Liquida total por consultor
        for ganancia in ganancias:
            total_ganancia = total_ganancia + ganancia.get('rl')

        # Calculo de todas las facturas generadas por el consultor
        cantidad_facturas = CaoFatura.objects.filter(
            co_os__in=orden_servicio
        ).annotate(
            year=ExtractYear('data_emissao')
        ).values('year').annotate(
            count=Count('co_os')
        ).values('count')

        for nf in cantidad_facturas:
            cantidad_facturas = nf.get('count')

        # Ganancias promedios generadas por el consultor en el periodo de
        # tiempo proporcionado como entrada
        if total_ganancia > 0:
            ganancias_promedio = total_ganancia / cantidad_facturas

            lista_bar.append(consultor_nombre)
            lista_bar.append(ganancias_promedio)
            data_bar[consultor_nombre] = lista_bar
            lista_bar = []
        else:
            lista_bar.append(consultor_nombre)
            lista_bar.append(0)
            data_bar[consultor_nombre] = lista_bar
            lista_bar = []

    # Costo fijo promedio de los consultores
    # TODO: Aqui se debe revisar bien, pues en la tabla CaoSalario faltan
    # muchas entradas de los consultores, hay fallas en la integridad de los
    # datos mirados como un conjunto para este calculo en especifico
    costo_fijo = CaoSalario.objects.exclude(
        brut_salario__in=[0]
    ).values('brut_salario')
    for cf in costo_fijo:
        costo_fijo_total = costo_fijo_total + cf.get('brut_salario')

    costo_fijo = CaoSalario.objects.exclude(
        brut_salario__in=[0]
    ).values('brut_salario')
    for cf in costo_fijo:
        cantidad_consultores = cantidad_consultores + 1

    costo_fijo_promedio = costo_fijo_total / cantidad_consultores
    data['data_bar'] = json.dumps(data_bar)
    data['costo_fijo_promedio'] = costo_fijo_promedio

    return render(request, 'desempenho/bar.html', data)
