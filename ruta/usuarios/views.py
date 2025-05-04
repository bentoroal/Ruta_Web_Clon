from django.shortcuts import render, redirect, get_object_or_404
from usuarios import models
from django.db import models
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from rest_framework import viewsets
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

#Vista para manejar la solicitud de inicio de sesion, que primero comprueba si esta ya logueado
#Si está logueado lo redirige al home, si no, lo redirigue al LoginView de Django

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Se mantiene el html de login

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario ya está autenticado
        if request.user.is_authenticated:
            return redirect('home')  # Redirige al usuario a la página de inicio
        # Continúa con el manejo predeterminado
        return super().dispatch(request, *args, **kwargs)


#Vista para crear cuenta de usuario
def signup(request):
    # Verifica si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')  # Redirige al usuario a la página de inicio
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})

#Vista para cerrar sesion
def logout(request):
    logout(request) # Cierra la sesión
    return redirect('login') # Redirige a la página de login


#Vistas que despliegan paginas simples

# Bienvenida al usuario
@login_required  # Asegura que sólo los usuarios autenticados puedan acceder
def bienvenida_view(request):
    # Se pasa el nombre de usuario para personalizar el mensaje de bienvenida'
    return render(request, 'bienvenida.html', {'nombre_usuario': request.user.username})

# Despedida a usuario que cierra sesion
def despedida_view(request):
    return render(request, "despedida.html")

# Pagina de inicio
def home_view(request):
    return render(request, "home.html")

# Pagina sobre la empresa
def nosotros_view(request):
    return render(request, "nosotros.html")

# Pagina sobre servicios de la empresa
def servicios_view(request):
    return render(request, "servicios.html")

# Pagina para contactar empresa
def contacto_view(request):
    return render(request, "contacto.html")


#Vistas con DRF
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

