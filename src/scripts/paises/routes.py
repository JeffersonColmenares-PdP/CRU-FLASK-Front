""" rutas del servicio 2 """

from flask import Blueprint

from . import controllers

#----------------- PRINCIPAL ------------------------------
servicio_2_blueprint = Blueprint(
    "servicio_2_blueprint",
    __name__,
    url_prefix='/servicio-2',
)

#-----------------TABLA PAISES ------------------------------
servicio_2_blueprint.add_url_rule(
    "/paises-espanol",
    view_func=controllers.cru_tabla_pais_espanol,
    methods=["GET", "POST", "PUT"]
)

#----------------TABLA TRADUCCIONES -------------------------------
servicio_2_blueprint.add_url_rule(
    "/nombre-pais-traducciones",
    view_func=controllers.cru_tabla_nombre_pais_traducciones,
    methods=["GET", "POST", "PUT"]
)

#--------------TABLA FRONTERAS ---------------------------------
servicio_2_blueprint.add_url_rule(
    "/fronteras",
    view_func=controllers.cru_tabla_fronteras,
    methods=["GET", "POST", "PUT"]
)

#---------------TABLA PERSONAJES--------------------------------
servicio_2_blueprint.add_url_rule(
    "/personajes",
    view_func=controllers.cru_tabla_personajes,
    methods=["GET", "POST", "PUT"]
)

#--------------TABLA ESPECIES---------------------------------
servicio_2_blueprint.add_url_rule(
    "/especies",
    view_func=controllers.cru_tabla_especies,
    methods=["GET", "POST", "PUT"]
)

#---------------TABLA UNION PAISES - PERSONAJES--------------------------------
servicio_2_blueprint.add_url_rule(
    "/union-pais-personaje",
    view_func=controllers.cru_union_pais_personaje,
    methods=["GET", "POST"]
)

#----------------TABLA UNION PAISES FRONTERAS -------------------------------
servicio_2_blueprint.add_url_rule(
    "/union-pais-fronteras",
    view_func=controllers.cru_union_pais_fronteras,
    methods=["GET", "POST"]
)