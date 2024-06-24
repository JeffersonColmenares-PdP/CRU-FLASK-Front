""" Controladores del servicio 1 """

# pylint: disable-all

from flask import request
import psycopg2
import json

from .queries import Query
from .clase_ejemplo import ClaseEjemplo


class ClasePokemon:
    """Clase ejemplo"""

    def __init__(self, nombre_pokemon, nombre_persona) -> None:
        pass

    datos_organizados = {"habilidaes": ["etc"]}


def endpoint_1():
    """Endpoint de ejemplo 1"""
    print("Ejecutano controlador")

    if not (
        "nombre_pokemon" in request.args.keys()
        and "nombre_persona" in request.args.keys()
    ):
        return "No se encontraron las llaves necesarias"

    nombre_pokemon = request.args.get("nombre_pokemon")
    nombre_persona = request.args.get("nombre_persona")

    datos_pokemon = ClasePokemon(nombre_pokemon, nombre_persona)

    return datos_pokemon.datos_organizados


def endpoint_2():
    """Endpoint de ejemplo 1"""

    datos_pokemon = ClaseEjemplo()
    datos_pokemon.validar(request.args)

    return datos_pokemon.datos_organizados

#-----------------------------------------------
def obtener_tabla_pais_espanol():
    try:
        nombre_tabla = "public.tabla_pais_espanol"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_espanol():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.tabla_pais_espanol
            (id_paises, nombre_paises, capital, area_km, continente, poblacion)
            VALUES ({entrada.get('id_paises')}, '{entrada.get('nombre_paises')}', '{entrada.get('capital')}', {entrada.get('area_km')}, '{entrada.get('continente')}', {entrada.get('poblacion')});
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_pais_espanol():
    if request.method == "GET":
        return obtener_tabla_pais_espanol()
    if request.method == "POST":
        return agregar_pais_espanol()

#-----------------------------------------------
def obtener_tabla_nombre_pais_traducciones():
    try:
        nombre_tabla = "public.tabla_nombre_pais_traducciones"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_traducciones():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.tabla_nombre_pais_traducciones
            (id_traduccion, nombre_idioma, traduccion_oficial, traduccion_comun, fk_pais)
            VALUES ({entrada.get('id_traduccion')}, '{entrada.get('nombre_idioma')}', '{entrada.get('traduccion_oficial')}', '{entrada.get('traduccion_comun')}', '{entrada.get('fk_pais')}');
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_nombre_pais_traducciones():
    if request.method == "GET":
        return obtener_tabla_nombre_pais_traducciones()
    if request.method == "POST":
        return agregar_pais_traducciones()

#-----------------------------------------------
def obtener_tabla_fronteras():
    try:
        nombre_tabla = "public.tabla_fronteras"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_fronteras():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.tabla_fronteras
            (id_frontera, nombre_frontera, longitud_frontera, descripcion_frontera, tipo_frontera)
            VALUES ({entrada.get('id_frontera')}, '{entrada.get('nombre_frontera')}', '{entrada.get('longitud_frontera')}', '{entrada.get('descripcion_frontera')}', '{entrada.get('tipo_frontera')}');
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_fronteras():
    if request.method == "GET":
        return obtener_tabla_fronteras()
    if request.method == "POST":
        return agregar_fronteras()

#-----------------------------------------------
def obtener_tabla_personajes():
    try:
        nombre_tabla = "public.tabla_personajes"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_personajes():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.tabla_personajes
            (id_personaje, nombre_personaje, genero, origen, fk_especie)
            VALUES ({entrada.get('id_personaje')}, '{entrada.get('nombre_personaje')}', '{entrada.get('genero')}', '{entrada.get('origen')}', '{entrada.get('fk_especie')}');
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_personajes():
    if request.method == "GET":
        return obtener_tabla_personajes()
    if request.method == "POST":
        return agregar_personajes()

#-----------------------------------------------
def obtener_tabla_especies():
    try:
        nombre_tabla = "public.tabla_especies"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_especies():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.tabla_especies
            (id_especie, nombre_especie, descripcion_especie, fecha_registro, alimentacion)
            VALUES ({entrada.get('id_especie')}, '{entrada.get('nombre_especie')}', '{entrada.get('descripcion_especie')}', '{entrada.get('fecha_registro')}', '{entrada.get('alimentacion')}');
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_especies():
    if request.method == "GET":
        return obtener_tabla_especies()
    if request.method == "POST":
        return agregar_especies()

#-----------------------------------------------
def obtener_union_pais_personaje():
    try:
        results = Query().buscar_union_pais_personaje()
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_personaje():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.union_pais_personaje
            (fk_pais, fk_personaje)
            VALUES ({entrada.get('fk_pais')}, {entrada.get('fk_personaje')});
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_union_pais_personaje():
    if request.method == "GET":
        return obtener_union_pais_personaje()
    if request.method == "POST":
        return agregar_pais_personaje()

#-----------------------------------------------
def obtener_union_pais_fronteras():
    try:
        nombre_tabla = "public.union_pais_fronteras"
        results = Query().buscar_tabla(nombre_tabla)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_frontera():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        query = f"""
            INSERT INTO public.union_pais_fronteras
            (fk_pais, fk_frontera)
            VALUES ({entrada.get('fk_pais')}, {entrada.get('fk_frontera')});
        """
        Query().agregar_datos(query)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_union_pais_fronteras():
    if request.method == "GET":
        return obtener_union_pais_fronteras()
    if request.method == "POST":
        return agregar_pais_frontera()







def agregar_pokemones():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_pokemon(entrada.get("id_pokemon"), entrada.get("nombre_pokemon"))
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }





