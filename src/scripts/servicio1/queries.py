""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_tabla(self, nombre_tabla: str):
        """
        It does nothing.
        """

        query = f"""
            SELECT * FROM {nombre_tabla}
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)

                return objeto_pais_espanol


    def buscar_union_pais_personaje(self):
        """
        It does nothing.
        """

        query = """
            SELECT p.nombre_paises, pj.nombre_personaje
            FROM union_pais_personaje AS u
            JOIN tabla_pais_espanol AS p ON u.fk_pais = p.id_paises
            JOIN tabla_personajes AS pj ON u.fk_personaje = pj.id_personaje;
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)

                return objeto_pais_espanol



    def buscar_union_pais_fronteras(self):
        """
        It does nothing.
        """

        query = """
            SELECT p.nombre_paises, pj.nombre_personaje
            FROM union_pais_fronteras AS u
            JOIN tabla_pais_espanol AS p ON u.fk_pais = p.id_paises
            JOIN tabla_fronteras AS f ON u.fk_frontera = f.id_frontera;
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)

                return objeto_pais_espanol




    def agregar_datos(self, query: str):
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)