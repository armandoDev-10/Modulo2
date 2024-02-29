from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from general.models import Reporte, Año
from pagos.models import Pago
from gastos.models import Fijo, Variable

from ingresos.models import Recuperadas, Remanente

# Create your views here.

@login_required
def MensualesList(request):
    reportes = Reporte.objects.all()

    context = {
        'reportes':reportes,
    }

    return render (request, 'reportes_mensuales.html', context)

@login_required
def ReporteDetail(request, pk):
    reporte = Reporte.objects.filter(id=pk)

    mes = reporte[0].mes
    aportacion = reporte[0].aportacion
    año = reporte[0].año

    pagos = Pago.objects.filter(mes=pk).order_by('edificio','departamento')
    
    contar_pagos = 0
    for i in range(len(pagos)):
        pago = str(pagos[i].status)

        if pago == 'Pagado':
            contar_pagos += 1
    
    print(contar_pagos)

    ingresos = aportacion * contar_pagos

    gastos_fijos = Fijo.objects.filter(mes=pk)
    gastos_variables = Variable.objects.filter(mes=pk)

    gastos_fijos_cantidad = 0
    gastos_variables_cantidad = 0

    for i in range(len(gastos_fijos)):
        cantidad = float(gastos_fijos[i].cantidad)

        gastos_fijos_cantidad += cantidad
    
    for i in range(len(gastos_variables)):
        cantidad = float(gastos_variables[i].cantidad)

        gastos_variables_cantidad += cantidad


    gastos = gastos_fijos_cantidad + gastos_variables_cantidad
    remanente = ingresos - gastos

    context= {
        'reporte':mes,
        'año':año,
        'aportacion':aportacion,
        'no_pagos':contar_pagos,

        'ingresos':r'{:,.1f}'.format(ingresos),
        'gastos':r'{:,.1f}'.format(gastos),
        'remanente':r'{:,.1f}'.format(remanente),

        'gastos_fijos':r'{:,.1f}'.format(gastos_fijos_cantidad),
        'gastos_variables':r'{:,.1f}'.format(gastos_variables_cantidad),

        'pagos':pagos,
        'gastos_fijos_list':gastos_fijos,
        'gastos_variables_list':gastos_variables,
    }

    return render(request, 'reporte.html', context)


@login_required
def AnualesList(request):
    reportes = Año.objects.all()

    context = {
        'reportes':reportes,
    }

    return render (request, 'reportes_anuales.html', context)

@login_required
def Reporte_anualDetail(request, pk):
    reportes = Reporte.objects.filter(año=pk)
    pagos_ = Pago.objects.filter(año=pk).order_by('mes','edificio','departamento')
    deudores = Pago.objects.filter(año=pk, status=2).order_by('edificio','departamento','mes')
    gastos_fijos_ = Fijo.objects.filter(año=pk).order_by('mes',)
    gastos_variables_ = Variable.objects.filter(año=pk).order_by('mes',)
    cuotas_recuperadas_list = Recuperadas.objects.filter(año=pk).order_by('mes', 'edificio', 'departamento')

    remanente_anterior = Remanente.objects.all()
    remanente_anterior_cantidad = float(remanente_anterior[0].cantidad)

    ingresos_anuales = []
    gastos_fijos_anuales = []
    gastos_variables_anuales = []
    no_pagos = []
    cuotas_recuperadas_anuales = []

    for i in range(len(reportes)):
        mes = reportes[i].mes
        mes_id = reportes[i].id
        aportacion = reportes[i].aportacion
        año = reportes[i].año

        pagos = Pago.objects.filter(año=pk, mes=mes_id)

        contar_pagos = 0
        for q in range(len(pagos)):
            pago = str(pagos[q].status)

            if pago == 'Pagado':
                contar_pagos += 1

        print(contar_pagos)
        no_pagos.append(contar_pagos)
        ingresos = aportacion * contar_pagos
        ingresos_anuales.append(ingresos)

        gastos_fijos = Fijo.objects.filter(año=pk,mes=mes_id)
        gastos_variables = Variable.objects.filter(año=pk,mes=mes_id)

        gastos_fijos_cantidad = 0
        gastos_variables_cantidad = 0

        for i in range(len(gastos_fijos)):
            cantidad = float(gastos_fijos[i].cantidad)

            gastos_fijos_cantidad += cantidad

        for i in range(len(gastos_variables)):
            cantidad = float(gastos_variables[i].cantidad)

            gastos_variables_cantidad += cantidad

        gastos_fijos_anuales.append(gastos_fijos_cantidad)
        gastos_variables_anuales.append(gastos_variables_cantidad)

        cuotas_recuperadas = Recuperadas.objects.filter(año=pk,mes=mes_id)
        cuotas_recuperadas_cantidad = 0

        for i in range(len(cuotas_recuperadas)):
            cantidad = float(cuotas_recuperadas[i].cantidad)

            cuotas_recuperadas_cantidad += cantidad
        
        cuotas_recuperadas_anuales.append(cuotas_recuperadas_cantidad)
    
    no_pagos = sum(no_pagos)
    ingresos_anuales = sum(ingresos_anuales)
    gastos_fijos_anuales = sum(gastos_fijos_anuales)
    gastos_variables_anuales = sum(gastos_variables_anuales)
    gastos_anuales = gastos_fijos_anuales + gastos_variables_anuales

    cuotas_recuperadas_anuales = sum(cuotas_recuperadas_anuales)
    ingresos_anuales = ingresos_anuales + cuotas_recuperadas_anuales

    remanente_anual = ingresos_anuales - gastos_anuales

    remanente_global = remanente_anual + remanente_anterior_cantidad

    context= {
        'reporte':mes,
        'año':año,
        'no_pagos':no_pagos,

        'ingresos':r'{:,.1f}'.format(ingresos_anuales),
        'cuotas_recuperadas':r'{:,.1f}'.format(cuotas_recuperadas_anuales),
        'gastos':r'{:,.1f}'.format(gastos_anuales),
        'remanente':r'{:,.1f}'.format(remanente_anual),

        'gastos_fijos':r'{:,.1f}'.format(gastos_fijos_anuales),
        'gastos_variables':r'{:,.1f}'.format(gastos_variables_anuales),

        'remanente_anterior':r'{:,.1f}'.format(remanente_anterior_cantidad),
        'remanente_global':r'{:,.1f}'.format(remanente_global),

        'pagos':pagos_,
        'gastos_fijos_list':gastos_fijos_,
        'gastos_variables_list':gastos_variables_,
        'cuotas_recuperadas_list':cuotas_recuperadas_list,
        'deudores':deudores,
    }

    return render(request, 'reporte_anual.html', context)
