from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	url(r'^$', inicio),
    url(r'^loguin/$', loguin),

    url(r'^docentes/$', docentes),
    url(r'^privado/$', privado),
    url(r'^salir/$', salir),
    url(r'^editarperfil/$',editar_perfil),
    url(r'^nuevo/$',nuevoUser.as_view(), name='nuevoUser'),
    url(r'^DatosUsuario/$', DatosUsuario, name='listaUsuarios'),
    url(r'^verificacion/$',verificacion, name='verificacion'),
    url(r'^informeReport/$', informeReport),

    url(r'^nuevoDirector/$',nuevoDirector.as_view(), name='nuevoDirector'),
    url(r'^verDitectores/$', verDitectores, name='verDitectores'),

    url(r'^nuevoAlumno/$',nuevoAlumno.as_view(), name='nuevoAlumno'),
    url(r'^verAlumno/$', verAlumno, name='verAlumno'),

    url(r'^regisrarse/$',regisrarseUser, name='regisrarse'),
    
    url(r'^perfilUser/$',perfilUser, name='perfilUser'),
    
    url(r'^bienvenida/$',bienvenida, name='bienvenida'),
    url(r'^personal/$',personal, name='personal'),
    url(r'^mensajes/$',mensajes, name='mensajes'),
    url(r'^buscar/$',buscar, name='buscar'),
    url(r'^newProducto/$',newProducto, name='newProducto'),
    url(r'^verProducto',verProducto, name='verProducto'),
    url(r'^Detalles/(?P<id>\d+)/$',Detalles),
    url(r'^EdirtarPro/(?P<id>\d+)/$',EdirtarPro),
    url(r'^ofertas/(?P<id>\d+)/$',ofertas),
    url(r'^dar_baja/(?P<id>\d+)/$',dar_baja),
    url(r'^like/(?P<id>\d+)/$',like),
)