""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_tabla_pais_espanol(self):
        """
        It does nothing.
        """

        query = """
            SELECT * FROM tabla_pais_espanol
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

    def buscar_tabla_nombre_pais_traducciones(self):
        """
        It does nothing.
        """

        query = """
            SELECT * FROM tabla_nombre_pais_traducciones
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

    def buscar_tabla_fronteras(self):
        """
        It does nothing.
        """

        query = """
            SELECT * FROM tabla_fronteras
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
            SELECT p.nombre_paises, f.nombre_frontera
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

    def insertar_personaje_pais(self, nombre_paises: str, nombre_personaje: str):
        #Consulta tabla_pais_espanol por nombre para traer id_paises
        query = f"""
            SELECT id_paises
            FROM tabla_pais_espanol
            WHERE nombre_paises = '{nombre_paises}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_paises = objeto_pais_espanol[0].get("id_paises")
        #Consulta tabla_personajes por nombre para traer id_personaje
        query = f"""
            SELECT id_personaje
            FROM tabla_personajes
            WHERE nombre_personaje = '{nombre_personaje}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_personaje = objeto_pais_espanol[0].get("id_personaje")
        #Consulta union_pais_personaje el id_paises y id_personaje
        query = f"""
            INSERT INTO public.union_pais_personaje
            (fk_pais, fk_personaje)
            VALUES ({id_paises}, {id_personaje});
            """
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def insertar_frontera_pais(self,  nombre_paises: str, nombre_frontera: str):
        #Consulta tabla_pais_espanol por nombre para traer id_paises
        query = f"""
            SELECT id_paises
            FROM tabla_pais_espanol
            WHERE nombre_paises = '{nombre_paises}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_paises = objeto_pais_espanol[0].get("id_paises")
        #Consulta tabla_fronteras por nombre para traer id_frontera
        query = f"""
            SELECT id_frontera
            FROM tabla_fronteras
            WHERE nombre_frontera = '{nombre_frontera}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_frontera = objeto_pais_espanol[0].get("id_frontera")
        #Consulta union_pais_fronteras el id_paises y id_frontera
        query = f"""
            INSERT INTO public.union_pais_fronteras
            (fk_pais, fk_frontera)
            VALUES ({id_paises}, {id_frontera});
            """
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)


    def actualizar_datos(self, query: str):
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)