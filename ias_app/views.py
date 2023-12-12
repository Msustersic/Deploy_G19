from rest_framework.viewsets import ModelViewSet

from .models import IaFunction
from .serializers import IaFunctionSerializer

from .models import Ia
from .serializers import IaSerializer

from .models import Comment
from .serializers import CommentSerializer

from .models import Curso
from .serializers import CursoSerializer 

from .models import Alumno
from .serializers import AlumnoSerializer

class IaFunctionViewSet(ModelViewSet):
   queryset = IaFunction.objects.all()
   serializer_class = IaFunctionSerializer

class IaViewSet(ModelViewSet):
   queryset = Ia.objects.all()
   serializer_class = IaSerializer

class CommentViewSet(ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer

class CursoViewSet(ModelViewSet):
   queryset = Curso.objects.all()
   serializer_class = CursoSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    