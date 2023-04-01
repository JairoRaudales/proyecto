from django.urls import re_path
from webapi.tipo_auto.view import tipo_auto_list, tipo_auto_marcas_list
from webapi.color.view import color_list
from webapi.genero.view import genero_list
from webapi.cliente.view import cliente_list, cliente_detail
from webapi.auto.view import auto_list, auto_detail
from webapi.auto.view import auto_color, auto_color_detail





urlpatterns = [
      re_path(r'^api/tipo_autos$', tipo_auto_list )
    , re_path(r'^api/tipo_autos/(?P<id>\d+)/marcas$', tipo_auto_marcas_list )
    
    , re_path(r'^api/colores$', color_list )
    , re_path(r'^api/generos$', genero_list )

    , re_path(r'^api/clientes$', cliente_list )
    , re_path(r'^api/clientes/(?P<id>\d+)$', cliente_detail )

    , re_path(r'^api/autos$', auto_list )
    , re_path(r'^api/autos/(?P<id>\d+)$', auto_detail )
    , re_path(r'^api/autos/(?P<id>\d+)/colores$', auto_color )
    , re_path(r'^api/autos/(?P<id>\d+)/colores/(?P<id_color>\d+)$', auto_color_detail )

]