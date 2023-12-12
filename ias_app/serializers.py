from rest_framework.serializers import ModelSerializer
from .models import IaFunction
from .models import Ia
from .models import Comment
from .models import Curso
from .models import Alumno
	
class IaFunctionSerializer(ModelSerializer):
   class Meta:
      model = IaFunction
      fields = "__all__"

class IaSerializer(ModelSerializer):
   class Meta:
      model = Ia
      fields = "__all__"

class CommentSerializer(ModelSerializer):
   class Meta:
      model = Comment
      fields = "__all__"

class CursoSerializer(ModelSerializer):
   class Meta:
      model = Curso
      fields = "__all__"

class AlumnoSerializer(ModelSerializer):
   class Meta:
      model = Alumno
      fields = "__all__"
