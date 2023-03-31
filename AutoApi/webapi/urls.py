from django.urls import re_path
from webapi.tipo_auto.view import tipo_auto_list, tipo_auto_marcas_list
from webapi.color.view import color_list
from webapi.genero.view import genero_list
#from webapi.observacion.view import observacion_list
from webapi.cliente.view import cliente_list, cliente_detail
from webapi.auto.view import auto_list, auto_detail
from webapi.auto.view import auto_colores, auto_colores_detail
from webapi.auto.view import auto_observacion, auto_observacion_detail




urlpatterns = [
      re_path(r'^api/tipo_autos$', tipo_auto_list )
    , re_path(r'^api/tipo_autos/(?P<id>\d+)/marcas$', tipo_auto_marcas_list )
    
    , re_path(r'^api/colores$', color_list )
    , re_path(r'^api/generos$', genero_list )
   # , re_path(r'^api/observaciones$', observacion_list )

    , re_path(r'^api/clientes$', cliente_list )
    , re_path(r'^api/clientes/(?P<id>\d+)$', cliente_detail )

    , re_path(r'^api/autos$', auto_list )
    , re_path(r'^api/autos/(?P<id>\d+)$', auto_detail )
    , re_path(r'^api/autos/(?P<id>\d+)/colores$', auto_colores )
    , re_path(r'^api/autos/(?P<id>\d+)/colores/(?P<id_color>\d+)$', auto_colores_detail )
    , re_path(r'^api/autos/(?P<id>\d+)/observaciones$', auto_observacion)
    , re_path(r'^api/autos/(?P<id>\d+)/observaciones/(?P<id_observacion>\d+)$', auto_observacion_detail )

]