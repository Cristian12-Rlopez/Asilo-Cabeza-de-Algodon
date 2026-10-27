from django.db import models

class Interno(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombres")
    apellido = models.CharField(max_length=100, verbose_name="Apellidos")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    motivo_reclusion = models.TextField(verbose_name="Motivo o Causa de Reclusión")
    psicopatologias = models.TextField(blank=True, null=True, verbose_name="Psicopatologías Base")
    medicinas_cajon = models.TextField(blank=True, null=True, verbose_name="Medicinas de Cajón")
    estado = models.CharField(max_length=50, default='Activo', verbose_name="Estado del Interno")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class FamiliarResponsable(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    cuota_mensual_fija = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    interno = models.OneToOneField(Interno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class VisitaMedica(models.Model):
    ESTADOS_PAGO = [
        ('Pendiente', 'Pendiente'),
        ('Abonada', 'Abonada'),
        ('Cancelada', 'Cancelada'),
    ]
    
    fecha_visita = models.DateField()
    medico_especialista = models.CharField(max_length=100)
    diagnostico = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2) # Con descuento aplicado
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='Pendiente')
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE)

    def __str__(self):
        return f"Visita de {self.interno} - {self.fecha_visita}"

class PagoFundacion(models.Model):
    # Tabla requerida para los pagos parciales o abonos a las citas de la fundación
    visita_medica = models.ForeignKey(VisitaMedica, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago de {self.monto} para Visita #{self.visita_medica.id}"

class MovimientoFinanciero(models.Model):
    TIPO_MOVIMIENTO = [
        ('Donacion', 'Donación'),
        ('Gasto', 'Gasto Operativo'),
        ('Pago', 'Pago de Cuota'),
    ]
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO)
    categoria = models.CharField(max_length=50) # Ejemplo: Luz, Agua, Mensualidad
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    interno = models.ForeignKey(Interno, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.monto}"

class Enfermero(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Enfermero(a)")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")

    def __str__(self):
        return self.nombre

class SolicitudRemision(models.Model):
    interno = models.ForeignKey(Interno, on_delete=models.CASCADE, verbose_name="Residente / Interno")
    evaluacion_inicial = models.TextField(verbose_name="Evaluación Médica Inicial")
    especialidad_requerida = models.CharField(max_length=100, verbose_name="Especialidad Requerida")
    enfermero_asignado = models.ForeignKey(Enfermero, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Enfermero Acompañante")
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Emisión")
    estado = models.CharField(max_length=50, default='Pendiente', verbose_name="Estado de Solicitud")

    def __str__(self):
        return f"Remisión #{self.id} - {self.interno}"

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

# Create your models here.
