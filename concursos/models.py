from django.db import models

# Create your models here.

class Asignatura(models.Model):

    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


class Llamado(models.Model):

    TIPO_LLAMADO = (
        ('CONVOCATORIA DE ASPIRANTES', 'Convocatoria de Aspirantes'),
        ('INSCRIPCION', 'Inscripcion'),
    )

    CARGO = (
        ('ASISTENTE', 'Asistente'),
        ('AYUDANTE', 'Ayudante'),
    )

    DEDICACION = (
        ('EXCLUSIVA', 'Exclusiva'),
        ('SEMIEXCLUSIVA', 'Semiexclusiva'),
        ('SIMPLE', 'Simple',)
    )

    tipo_llamado = models.CharField(choices=TIPO_LLAMADO, max_length=100)
    cargo = models.CharField(choices=CARGO, max_length=100, default='ASISTENTE' )
    #categoria =
    dedicacion = models.CharField(choices=DEDICACION, max_length=100, default='SIMPLE')
    #area = 
    asignatura = models.ManyToManyField(Asignatura, verbose_name="Lista de Asignaturas")
    #tareas_a_cumplir =
    #lugar =
    fecha_apertura = models.DateTimeField(null=True, blank=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=False, verbose_name="Publicado")
    #requisitos =
    #comision_ad_hoc =
    #jurado_suplente 

    def __str__(self):
        return self.tipo_llamado

    
    def display_asignatura(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ asignatura.nombre for asignatura in self.asignatura.all()[:3] ])
    display_asignatura.short_description = 'Asignatura'