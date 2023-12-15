
from django.contrib import admin 
from django.urls import path , include


from .views import IndexPage
from .views import Funcion
from .views import Comentarios
from .views import Login
from .views import Dejar_comentario
from .views import Editar
from .views import Crear

from .views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("/comentarios", Comentarios.as_view(), name="comentarios"),
    path("/login", Login.as_view(), name="login"),
    path("/dejar_comentario", Dejar_comentario.as_view(), name="dejar_comentario"),
    path("/edit", Editar.as_view(), name="edit"),
    path("/crear", Crear.as_view(), name="crear"),
    path("store/", include("store_app.urls")),
    path('logout/', logout_view, name='logout'),

]

