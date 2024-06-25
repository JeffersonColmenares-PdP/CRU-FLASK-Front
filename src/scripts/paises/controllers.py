""" Controladores del servicio 2 = paises """

# pylint: disable-all

from flask import request
import psycopg2

from .queries import Query

#-----------------TABLA PAISES ------------------------------
def obtener_tabla_pais_espanol():
    try:
        
        results = Query().buscar_tabla_pais_espanol
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

def actualizar_pais_espanol():
    try:
        entrada = request.json
        if "id_paises" not in entrada:
            return {"msg": "El id_paises es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_pais_espanol
                SET {datos} = '{entrada[datos]}'
                WHERE id_paises = {entrada.get('id_paises')};
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

def cru_tabla_pais_espanol():
    if request.method == "GET":
        return obtener_tabla_pais_espanol()
    if request.method == "POST":
        return agregar_pais_espanol()
    if request.method == "PUT":
        return actualizar_pais_espanol()

#----------------TABLA TRADUCCIONES -------------------------------
def obtener_tabla_nombre_pais_traducciones():
    try:
        nombre_tabla = "public.tabla_nombre_pais_traducciones"
        results = Query().buscar_tabla_nombre_pais_traducciones
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

def actualizar_pais_traducciones():
    try:
        entrada = request.json
        if "id_traduccion" not in entrada:
            return {"msg": "El id_traduccion es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_nombre_pais_traducciones
                SET {datos} = '{entrada[datos]}'
                WHERE id_traduccion = {entrada.get('id_traduccion')};
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

def cru_tabla_nombre_pais_traducciones():
    if request.method == "GET":
        return obtener_tabla_nombre_pais_traducciones()
    if request.method == "POST":
        return agregar_pais_traducciones()
    if request.method == "PUT":
        return actualizar_pais_traducciones()

#--------------TABLA FRONTERAS ---------------------------------
def obtener_tabla_fronteras():
    try:
        nombre_tabla = "public.tabla_fronteras"
        results = Query().buscar_tabla_fronteras
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

def actualizar_tabla_fronteras():
    try:
        entrada = request.json
        if "id_frontera" not in entrada:
            return {"msg": "El id_frontera es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_fronteras
                SET {datos} = '{entrada[datos]}'
                WHERE id_frontera = {entrada.get('id_frontera')};
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

def cru_tabla_fronteras():
    if request.method == "GET":
        return obtener_tabla_fronteras()
    if request.method == "POST":
        return agregar_fronteras()
    if request.method == "PUT":
        return actualizar_tabla_fronteras()


    if request.method == "GET":
        return obtener_union_pais_fronteras()
    if request.method == "POST":
        return agregar_pais_frontera()
    

#----------------TABLA UNION PAISES FRONTERAS -------------------------------
def obtener_union_pais_fronteras():
    try:
        results = Query().buscar_union_pais_fronteras()
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
        Query().insertar_frontera_pais(entrada.get("nombre_paises"), entrada.get("nombre_frontera"))
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
