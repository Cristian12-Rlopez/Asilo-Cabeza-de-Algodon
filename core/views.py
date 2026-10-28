from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (
    Interno, FamiliarResponsable, MedicoEspecialista, Enfermero,
    SolicitudRemision, AgendaCita, ConsultaMedica, OrdenLaboratorio,
    VisitaMedica, PagoFundacion, Donacion, GastoOperativo,
    DescuentoFundacion, CuentaPorPagar, CuotaFamiliar
)

# Vista pública para usuarios generales (Landing Page)
def inicio(request):
    return render(request, 'inicio.html')

# Vista del portal de usuarios
def panel_usuario(request):
    return render(request, 'panel_usuario.html')

# Nueva vista del dashboard protegida con login
@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html', {
        'usuario': request.user
    })

@login_required
def expedientes_view(request):
    # Consultamos todos los expedientes ordenados por fecha de creación
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/expedientes.html', {
        'usuario': request.user,
        'internos': internos
    })

@login_required
def motivos_reclusion_view(request):
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/motivos_reclusion.html', {'usuario': request.user, 'internos': internos})

@login_required
def ficha_medica_view(request):
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/ficha_medica.html', {'usuario': request.user, 'internos': internos})

@login_required
def psicopatologias_view(request):
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/psicopatologias.html', {'usuario': request.user, 'internos': internos})

@login_required
def historial_clinico_view(request):
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/historial_clinico.html', {'usuario': request.user, 'internos': internos})

@login_required
def evaluaciones_iniciales_view(request):
    solicitudes = SolicitudRemision.objects.all().order_by('-fecha_emision')
    return render(request, 'core/evaluaciones_iniciales.html', {'usuario': request.user, 'solicitudes': solicitudes})

@login_required
def remisiones_web_view(request):
    solicitudes = SolicitudRemision.objects.all().order_by('-fecha_emision')
    return render(request, 'core/remisiones_web.html', {'usuario': request.user, 'solicitudes': solicitudes})

@login_required
def asignacion_enfermeros_view(request):
    solicitudes = SolicitudRemision.objects.all()
    return render(request, 'core/asignacion_enfermeros.html', {'usuario': request.user, 'solicitudes': solicitudes})

@login_required
def agenda_citas_view(request):
    citas = AgendaCita.objects.all().order_by('-fecha_hora_cita')
    return render(request, 'core/agenda_citas.html', {'usuario': request.user, 'citas': citas})

@login_required
def notificacion_smtp_view(request):
    solicitudes = SolicitudRemision.objects.all().order_by('-fecha_emision')
    return render(request, 'core/notificacion_smtp.html', {'usuario': request.user, 'solicitudes': solicitudes})

@login_required
def consultas_especializadas_view(request):
    consultas = ConsultaMedica.objects.all().order_by('-fecha_consulta')
    return render(request, 'core/consultas_especializadas.html', {'usuario': request.user, 'consultas': consultas})

@login_required
def diagnostico_observaciones_view(request):
    consultas = ConsultaMedica.objects.all().order_by('-fecha_consulta')
    return render(request, 'core/diagnostico_observaciones.html', {'usuario': request.user, 'consultas': consultas})

@login_required
def ordenes_laboratorio_view(request):
    ordenes = OrdenLaboratorio.objects.all().order_by('-fecha_solicitud')
    return render(request, 'core/ordenes_laboratorio.html', {'usuario': request.user, 'ordenes': ordenes})

@login_required
def carga_resultados_view(request):
    ordenes = OrdenLaboratorio.objects.all().order_by('-fecha_solicitud')
    return render(request, 'core/carga_resultados.html', {'usuario': request.user, 'ordenes': ordenes})

@login_required
def recetas_farmacia_view(request):
    consultas = ConsultaMedica.objects.all().order_by('-fecha_consulta')
    return render(request, 'core/recetas_farmacia.html', {'usuario': request.user, 'consultas': consultas})

@login_required
def descuentos_fundacion_view(request):
    descuentos = DescuentoFundacion.objects.all().order_by('-fecha')
    return render(request, 'core/descuentos_fundacion.html', {'usuario': request.user, 'descuentos': descuentos})

@login_required
def cuentas_pagar_view(request):
    cuentas = CuentaPorPagar.objects.all().order_by('fecha_vencimiento')
    return render(request, 'core/cuentas_pagar.html', {'usuario': request.user, 'cuentas': cuentas})

@login_required
def cargos_cuotas_view(request):
    cargos = CuotaFamiliar.objects.all().order_by('-id')
    return render(request, 'core/cargos_cuotas.html', {'usuario': request.user, 'cargos': cargos})

@login_required
def registro_donaciones_view(request):
    donaciones = Donacion.objects.all().order_by('-id')
    return render(request, 'core/registro_donaciones.html', {'usuario': request.user, 'donaciones': donaciones})

@login_required
def gastos_operativos_view(request):
    gastos = GastoOperativo.objects.all().order_by('-fecha')
    return render(request, 'core/gastos_operativos.html', {'usuario': request.user, 'gastos': gastos})

@login_required
def reportes_clinicos_view(request):
    internos = Interno.objects.all().order_by('-id')
    return render(request, 'core/reportes_clinicos.html', {'usuario': request.user, 'internos': internos})

@login_required
def balance_ingresos_view(request):
    donaciones = Donacion.objects.all().order_by('-id')
    return render(request, 'core/balance_ingresos.html', {'usuario': request.user, 'donaciones': donaciones})

@login_required
def estado_egreso_view(request):
    gastos = GastoOperativo.objects.all().order_by('-fecha')
    return render(request, 'core/estado_egreso.html', {'usuario': request.user, 'gastos': gastos})

@login_required
def control_costos_view(request):
    citas = AgendaCita.objects.all().order_by('-fecha_hora_cita')
    return render(request, 'core/control_costos.html', {'usuario': request.user, 'citas': citas})

@login_required
def exportacion_pdf_excel_view(request):
    return render(request, 'core/exportacion_pdf_excel.html', {'usuario': request.user})
