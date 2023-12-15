from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


class IndexPage(TemplateView):
    template_name = "index.html"

class Funcion(TemplateView):
    template_name = "byFunction.html"

class Comentarios(TemplateView):
    template_name = "comments.html"

class Login(TemplateView):
    template_name = "fLogin.html"

class Dejar_comentario(TemplateView):
    template_name = "fComments.html"

class Editar(TemplateView):
    template_name = "edit.html"

class Crear(TemplateView):
    template_name = "fNewIA.html"

def logout_view(request):
    logout(request)
    return redirect('index')

