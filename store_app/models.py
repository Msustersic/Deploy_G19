from django.db import models
from django.db import models
from django.db.models import Model


class Store(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    id = models.FloatField(primary_key=True,blank=False, default=1)
    nombre  =  models.CharField(max_length=200, default="...")
    link  = models.CharField(max_length=800, default="...")
    imagen =  models.CharField(max_length=200, default="...")

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta: 
        db_table = "ias" # Definimos el nombre de la tabla

    def __str__(self):
        return f"La IA: {self.nombre}, su link es: {self.link}"

    def get_fields(self): # Aca se traen todos los atributos excepto el nombre
        """
        Obtiene los campos y sus valores asociados de un objeto.

        Retorna una lista de tuplas donde cada tupla contiene el nombre legible
        del campo y el valor correspondiente del objeto actual.

        Nota:
        - La función utiliza los metadatos del modelo (self.__class__._meta.fields)
        para obtener la lista de campos, excluyendo el primer campo que generalmente
        es la clave primaria.
        - La tupla resultante tiene el formato (nombre_legible_del_campo, valor_del_campo).

        Ejemplo:
        Si tienes un modelo `MiModelo` con campos 'nombre' y 'edad', y un objeto `obj`
        de ese modelo con nombre='Juan' y edad=25, llamar a `obj.get_fields()` podría
        retornar [('nombre', 'Juan'), ('edad', 25)].

        Returns:
        List[tuple]: Lista de tuplas donde cada tupla contiene el nombre del campo
                    y el valor asociado del objeto actual.
        """
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]

