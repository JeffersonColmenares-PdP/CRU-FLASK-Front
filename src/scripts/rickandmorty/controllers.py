""" Controladores del servicio 1 """

# pylint: disable-all

from flask import request
import psycopg2

from .queries import Query

#---------------TABLA PERSONAJES--------------------------------
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

def actualizar_tabla_personajes():
    try:
        entrada = request.json
        if "id_personaje" not in entrada:
            return {"msg": "El id_personaje es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_personajes
                SET {datos} = '{entrada[datos]}'
                WHERE id_personaje = {entrada.get('id_personaje')};
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
        "msg": "Se actualizo satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_personajes():
    if request.method == "GET":
        return obtener_tabla_personajes()
    if request.method == "POST":
        return agregar_personajes()
    if request.method == "PUT":
        return actualizar_tabla_personajes()

#--------------TABLA ESPECIES---------------------------------
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

def actualizar_tabla_especies():
    try:
        entrada = request.json
        if "id_especie" not in entrada:
            return {"msg": "El id_especie es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_especies
                SET {datos} = '{entrada[datos]}'
                WHERE id_especie = {entrada.get('id_especie')};
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
        "msg": "Se actualizo satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_especies():
    if request.method == "GET":
        return obtener_tabla_especies()
    if request.method == "POST":
        return agregar_especies()
    if request.method == "PUT":
        return actualizar_tabla_especies()

#---------------TABLA UNION PAISES - PERSONAJES--------------------------------
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
        Query().insertar_personaje_pais(entrada.get("nombre_paises"), entrada.get("nombre_personaje"))
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
