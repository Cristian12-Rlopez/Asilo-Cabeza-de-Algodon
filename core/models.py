from django.db import models

class Interno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True, blank=True) # <-- Soluciona el error de fecha_creacion
    # habitacion = models.CharField(max_length=20, null=True, blank=True)
    motivo_reclusion = models.TextField()
    psicopatologias = models.TextField(blank=True, null=True)
    medicinas_de_cajon = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='Activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class FamiliarResponsable(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, related_name='familiares')
    nombre_completo = models.CharField(max_length=150, default="")
    parentesco = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nombre_completo} ({self.parentesco})"

class MedicoEspecialista(models.Model):
    nombre = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Dr(a). {self.nombre} - {self.especialidad}"

class Enfermero(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

class SolicitudRemision(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, related_name='solicitudes')
    fecha_emision = models.DateField(auto_now_add=True)
    evaluacion_inicial = models.TextField()
    especialidad_requerida = models.CharField(max_length=100)
    enfermero_asignado = models.ForeignKey(Enfermero, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=30, default='Pendiente')

    def __str__(self):
        return f"Remisión para {self.interno} ({self.especialidad_requerida})"

class AgendaCita(models.Model):
    solicitud = models.OneToOneField(SolicitudRemision, on_delete=models.CASCADE, verbose_name="Solicitud Base")
    fecha_hora_cita = models.DateTimeField(verbose_name="Fecha y Hora de la Cita")
    medico_especialista = models.CharField(max_length=100, verbose_name="Médico Especialista Asignado")
    estado_cita = models.CharField(max_length=50, default='Agendada', verbose_name="Estado de Cita")

    def __str__(self):
        return f"Cita con {self.medico_especialista} ({self.fecha_hora_cita})"

class ConsultaMedica(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, verbose_name="Residente / Interno")
    medico_especialista = models.CharField(max_length=100, verbose_name="Médico Especialista")
    fecha_consulta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Consulta")
    diagnostico = models.TextField(verbose_name="Diagnóstico u Observaciones")
    tratamiento_recetado = models.TextField(blank=True, null=True, verbose_name="Receta / Medicamentos")

    def __str__(self):
        return f"Consulta {self.interno} - {self.medico_especialista}"

class OrdenLaboratorio(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE, verbose_name="Consulta Médica Asociada")
    tipo_examen = models.CharField(max_length=150, verbose_name="Tipo de Examen Requerido")
    resultado = models.TextField(blank=True, null=True, verbose_name="Resultado Digital / Informe")
    estado = models.CharField(max_length=50, default='Pendiente', verbose_name="Estado de Orden")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")

    def __str__(self):
        return f"Examen: {self.tipo_examen} ({self.consulta.interno})"

class VisitaMedica(models.Model):
    solicitud = models.OneToOneField(SolicitudRemision, on_delete=models.SET_NULL, null=True, blank=True)
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, related_name='visitas')
    medico_especialista = models.ForeignKey(MedicoEspecialista, on_delete=models.SET_NULL, null=True)
    fecha_visita = models.DateField()
    diagnostico = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado_pago = models.CharField(max_length=30, default='Pendiente')

    def __str__(self):
        return f"Visita a {self.interno} - {self.fecha_visita}"

class PagoFundacion(models.Model):
    visita = models.ForeignKey(VisitaMedica, on_delete=models.CASCADE, related_name='pagos', null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pago = models.CharField(max_length=50, default='Efectivo/Transferencia')

    def __str__(self):
        return f"Pago de Q{self.monto} para Visita #{self.visita_id}"

class Donacion(models.Model):
    TIPO_DONANTE = [
        ('Empresa Internacional', 'Empresa Internacional'),
        ('Empresa Nacional', 'Empresa Nacional'),
        ('Gobierno', 'Gobierno'),
        ('Particular', 'Particular'),
    ]
    donante = models.CharField(max_length=150)
    tipo_donacion = models.CharField(max_length=50, choices=TIPO_DONANTE, default='Particular')
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.donante} - Q{self.monto}"

class GastoOperativo(models.Model):
    CATEGORIA_GASTO = [
        ('Luz', 'Luz'),
        ('Agua', 'Agua'),
        ('Otros', 'Otros'),
    ]
    concepto = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_GASTO)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.concepto} - Q{self.monto}"

class DescuentoFundacion(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, verbose_name="Residente / Interno")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto de Descuento (Q)")
    motivo = models.CharField(max_length=200, verbose_name="Motivo del Descuento")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de Aplicación")

    def __str__(self):
        return f"Descuento Q{self.monto} - {self.interno}"

class CuentaPorPagar(models.Model):
    concepto = models.CharField(max_length=150, verbose_name="Concepto / Proveedor")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Pendiente (Q)")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    estado = models.CharField(max_length=50, default='Pendiente', verbose_name="Estado de Pago")

    def __str__(self):
        return f"CxP: {self.concepto} (Q{self.monto})"

class CuotaFamiliar(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, verbose_name="Residente / Interno")
    monto_cuota = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto de Cuota (Q)")
    mes_correspondiente = models.CharField(max_length=50, verbose_name="Mes / Periodo")
    pagado = models.BooleanField(default=False, verbose_name="¿Pagado?")

    def __str__(self):
        return f"Cuota {self.mes_correspondiente} - {self.interno}" 

#hay errores asi que con este comentario se fuerzan las columnas a que se actualicen en Aiven
# Create your models here.
