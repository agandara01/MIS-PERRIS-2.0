from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from registro import views

router = routers.DefaultRouter()
router.register(r'personas', views.PersonaViewSet)
router.register(r'articulos', views.ArticuloViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('donar',views.donar,name="donar"),
    path('donar/crearD',views.crearD,name="crearD"),
    path('donar/eliminarD/<int:id>',views.eliminarD,name="eliminarD"),
    path('cerrarsession2',views.cerrar_session2,name="cerrar_session2"),
    path('registro/crear',views.crear,name="crear"),
    path('registro/eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('registro/editar',views.editar,name="editar"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('inicio',views.inicio,name="inicio"),
    path('hola',views.hola,name="hola"),
    path('contacto',views.contacto,name="contacto"),
    url(r'^salir/$',views.logOut,name='logOut'),
    # Necesario para allauth
    path('accounts/', include('allauth.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

