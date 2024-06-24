""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_1_blueprint = Blueprint(
    "servicio_1_blueprint",
    __name__,
    url_prefix='/servicio-1',
)

servicio_1_blueprint.add_url_rule(
    "/ejemplo",
    view_func=controllers.endpoint_1,
    methods=["GET"]
)
servicio_1_blueprint.add_url_rule(
    "/ejemplo-body",
    view_func=controllers.endpoint_2,
    methods=["POST"]
)

servicio_1_blueprint.add_url_rule(
    "/paises-espanol",
    view_func=controllers.cru_tabla_pais_espanol,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/nombre-pais-traducciones",
    view_func=controllers.cru_tabla_nombre_pais_traducciones,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/fronteras",
    view_func=controllers.cru_tabla_fronteras,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/personajes",
    view_func=controllers.cru_tabla_personajes,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/especies",
    view_func=controllers.cru_tabla_especies,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/union_pais_personaje",
    view_func=controllers.cru_union_pais_personaje,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/union_pais_fronteras",
    view_func=controllers.cru_union_pais_fronteras,
    methods=["GET", "POST"]
)