from django.urls import path, include
from usuarios import views 
from .views import CustomLoginView, UserViewSet
from django.contrib.auth import views as auth_views #Se importan views de autenticacion de django
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/users', UserViewSet, basename='user')

urlpatterns = [

    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('bienvenida/', views.bienvenida_view, name='bienvenida'),
    path('despedida/', views.despedida_view, name='despedida'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('nosotros/', views.nosotros_view, name='nosotros'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('contacto/', views.contacto_view, name='contacto'),

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    #  Incluye las rutas de la API
    path('', include(router.urls)),
]
    