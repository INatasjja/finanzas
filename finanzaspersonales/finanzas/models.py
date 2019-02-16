from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class TipoEgresos(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID tipo de egreso")
    descripcion = models.CharField(max_length=50, help_text="Descripcion del tipo de Egreso")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del egreso')
    # Métodos
    def __str__(self):
        return "{}".format(self.descripcion)


class TipoIngresos(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID tipo de ingreso")
    descripcion = models.CharField(max_length=50, help_text="Descripcion del tipo de Ingreso")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del Ingreso')
    # Métodos
    def __str__(self):
        return "{}".format(self.descripcion)


class RenglonEgresos(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID renglon de egreso")
    descripcion = models.CharField(max_length=50, help_text="Renglones de Egresos")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del renglon')
    # Métodos
    def __str__(self):
        return "{}".format(self.descripcion)


class TipoPago(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID tipo de pago")
    descripcion = models.CharField(max_length=50, help_text="Tipo de Pago")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del tipo de pago')
    # Métodos
    def __str__(self):
        return "{}".format(self.descripcion)



class GestionEgresos(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Gestion de Egresos")
    tipo = models.ForeignKey('TipoEgresos', on_delete=models.SET_NULL, null=True, verbose_name ='Tipo de Egreso')
    renglon = models.ForeignKey('RenglonEgresos', on_delete=models.SET_NULL, null=True, verbose_name ='Renglon')
    tipopago = models.ForeignKey('TipoPago', on_delete=models.SET_NULL, null=True, default='X', verbose_name ='Tipo de pago')
    descripcion = models.CharField(max_length=50, help_text="Descripcion", verbose_name ='Descripcion')
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del tipo de pago', verbose_name ='Estado')
    
    # Métodos
    def __str__(self):
        return self.descripcion



class FuenteIngreso(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Fuente de Ingreso")
    descripcion = models.CharField(max_length=50, help_text="Descripcion")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado Fuente de Ingreso')
    # Métodos
    def __str__(self):
        return self.descripcion



class GestionIngresos(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Gestion de Egresos")
    tipo = models.ForeignKey('TipoIngresos', on_delete=models.SET_NULL, null=True, verbose_name ='Tipo de Egreso')
    descripcion = models.CharField(max_length=50, help_text="Descripcion", verbose_name ='Descripcion')
    fuente = models.ForeignKey('FuenteIngreso', on_delete=models.SET_NULL, null=True, verbose_name ='Fuente de Ingreso')
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del tipo de pago', verbose_name ='Estado')
    
    # Métodos
    def __str__(self):
        return self.descripcion


class usuarios(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Usuario")
    primernombre = models.CharField(max_length=15, help_text="Primer Nombre", verbose_name ="Primer Nombre")
    segundonombre  = models.CharField(max_length=15, help_text="Segundo Nombre", verbose_name ="Segundo Nombre")
    primerapellido = models.CharField(max_length=15, help_text="Primer Apellido", verbose_name ="Primer Apellido")
    segundoapellido = models.CharField(max_length=15, help_text="Segundo Apellido", verbose_name ="Segundo Apellido")
    cedula = models.CharField(max_length=11, help_text="Cedula", verbose_name = "Cedula")
    limiteegresos = models.IntegerField(validators=[MinValueValidator(0)],default=0, help_text='Limite de Egresos', verbose_name ='Limite de Egresos')
    tipopersona = models.CharField(max_length=1, choices=(('F', 'Fisica'),('J', 'Juridico')), blank=True, default='A', help_text='Tipo de persona, Fisica o Juridica', verbose_name ='Tipo Persona')
    fechacorte = models.DateField(help_text='Fecha de Corte', verbose_name ='Fecha de Corte')
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado del tipo de pago', verbose_name ='Estado')
    
    # Métodos
    def __str__(self):
        return "{} {} {} {}".format(self.primernombre, 
                                    self.segundonombre, 
                                    self.primerapellido, 
                                    self.segundoapellido)



class Transacciones(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Transaccion")
    tipotransaccion = models.CharField(max_length=1, choices=(('I', 'Ingreso'),('E', 'Egreso')), blank=True, default='A', help_text='Tipo de Ingreso', verbose_name ='Tipo de Ingreso')
    usuario = models.ForeignKey('usuarios', on_delete=models.SET_NULL, null=True, verbose_name ='Usuario')
    tipo = models.CharField(max_length=1, choices=(('I', 'Ingreso'),('G', 'Gasto')), blank=True, default='A', help_text='Tipo de Transaccion', verbose_name ='Tipo de Transaccion')
    tipopago = models.ForeignKey('TipoIngresos', on_delete=models.SET_NULL, null=True, verbose_name ='Tipo de Pago')
    fechatransaccion = models.DateField(help_text='Fecha de la transaccion', verbose_name ='Fecha de la transaccion')
    fecharegistro = models.DateField(default=timezone.now,help_text='Fecha de registro', verbose_name ='Fecha de registro')
    monto = models.IntegerField(validators=[MinValueValidator(0)],default=0, help_text='Monto Transaccion', verbose_name ='Monto Transaccion')
    notarjeta = models.CharField(max_length=100, help_text="Numero de tarjeta CR", verbose_name ="Numero de tarjeta CR")
    comentario = models.CharField(max_length=100, help_text="Comentario", verbose_name ="Comentario")
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'),('I', 'Inactivo')), blank=True, default='A', help_text='Estado', verbose_name ='Estado')
    
    # Métodos
    def __str__(self):
        return "{} {}".format(self.tipopago,self.usuario,)



class Corte(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID Transaccion")
    ano = models.IntegerField(validators=[MinValueValidator(0)],help_text='Año', verbose_name ='Año')
    mes = models.IntegerField(validators=[MinValueValidator(1)],help_text='Mes', verbose_name ='Mes')
    fechacorte = models.DateField(default=timezone.now,help_text='Fecha del Corte', verbose_name ='Fecha del Corte')
    balanceinicial = models.IntegerField(validators=[MinValueValidator(0)],default=0,help_text='Balance Inicial', verbose_name ='Balance Inicial')
    totalingresos = models.IntegerField(validators=[MinValueValidator(0)],default=0,help_text='Total Ingresos', verbose_name ='Total Ingresos')
    totalegresos = models.IntegerField(validators=[MinValueValidator(0)],default=0,help_text='Total Egresos', verbose_name ='Total Egresos')
    balancecorte = models.IntegerField(validators=[MinValueValidator(0)],default=0,help_text='Balance Al Corte', verbose_name ='Balance Al Corte')
    # Métodos
    def __str__(self):
        return self.descripcion