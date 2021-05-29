from neo4j import GraphDatabase, WRITE_ACCESS
import Code.DB_Nodos as nodos


def crear_relacion(usuario, categoria, relacion, nodo):
    query = f"MATCH ({usuario}:User {{nombre:\"{usuario}\"}}), ({nodo}:{categoria} {{nombre:\"{nodo}\"}}) " \
            f"CREATE ({usuario})-[:{relacion}]->({nodo}) "
    return query


class DB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def base(self):
        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        noditos = nodos.Nodos().creador_nodos()
        relaciones = nodos.Nodos().relacions_DB_total()
        session.run(noditos)
        for usuario in relaciones:
            for relacion in usuario:
                session.run(relacion)
        session.close()

    def match(self, nodo_nivel_usuario, relacion_modalidad_nivel, relacion_apertura_o_defensa, apertura_defensa_nodo):
        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        query = f"MATCH ({nodo_nivel_usuario}:Nivel {{nombre:\"{nodo_nivel_usuario}\"}})<-[:{relacion_modalidad_nivel}]-(User)-[r:{relacion_apertura_o_defensa}]->({apertura_defensa_nodo}) RETURN {apertura_defensa_nodo}.nombre, count(r) AS num ORDER BY num desc"
        result = session.run(query)
        vacio = []
        for element in result:
            vacio.append(element["Apertura.nombre"])
        session.close()
        listafinal = ','.join(str(elemento) for elemento in vacio)
        listafinal = listafinal.split(",")
        return listafinal

    def queries_user_nuevo(self, USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA):
        query_nodo_user: str = f"CREATE ({USER.lower()}:User {{nombre:\"{USER.lower()}\"}})"
        categorias = ["Nivel", "Plataforma", "Apertura", "Defensa", "Favorito"]
        relacions = ["NIVEL_BLITZ", "NIVEL_RAPIDAS", "PARTE_FAVORITA", "PLATAFORMA", "APERTURA", "DEFENSA"]
        query_relacion_nivel_blitz: str = crear_relacion(USER, categorias[0], relacions[0], NIVEL_BLITZ)
        query_relacion_nivel_rapidas: str = crear_relacion(USER, categorias[0], relacions[1], NIVEL_RAPIDAS)
        query_relacion_parte_favorita: str = crear_relacion(USER, categorias[4], relacions[2], PARTE_FAVORITA)
        query_relacion_plataforma: str = crear_relacion(USER, categorias[1], relacions[3], PLATAFORMA)
        query_relacion_apertura: str = crear_relacion(USER, categorias[2], relacions[4], APERTURA)
        query_relacion_defensa: str = crear_relacion(USER, categorias[3], relacions[5], DEFENSA)
        return query_nodo_user, query_relacion_nivel_blitz, query_relacion_nivel_rapidas, query_relacion_parte_favorita, query_relacion_plataforma, query_relacion_apertura, query_relacion_defensa

    def crear_user(self, USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA):
        query_nodo_user, query_relacion_nivel_blitz, query_relacion_nivel_rapidas, query_relacion_parte_favorita, query_relacion_plataforma, query_relacion_apertura, query_relacion_defensa = self.queries_user_nuevo(USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA)

        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        session.run(query_relacion_apertura)
        session.run(query_nodo_user)
        session.run(query_relacion_nivel_blitz)
        session.run(query_relacion_nivel_rapidas)
        session.run(query_relacion_parte_favorita)
        session.run(query_relacion_plataforma)
        session.run(query_relacion_apertura)
        session.run(query_relacion_defensa)
        session.close()


    def borrar_user(self, user):
        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        query = f"MATCH (n {{nombre: '{user}'}}) DETACH DELETE n"
        session.run(query)
        session.close()

    def borrar_DB(self):
        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        query = "MATCH (n) DETACH DELETE n"
        session.run(query)
        session.close()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    greeter = DB("bolt://localhost:11006", "neo4j", "12345")
    #greeter.base()
    # print(greeter.match("principiante", "NIVEL_BLITZ", "APERTURA", "Apertura"))
    #greeter.borrar_user("user002")
    #greeter.crear_user("user050", "principiante", "principiante", "final", "chess24", "italiana_espanola", "francesa")
    #greeter.borrar_DB()


    greeter.close()

#print(crear_relacion("USER", "lol", "jaja", "jeje"))

"""
MATCH (nodo:Nivel {nombre:"principiante"})<-[:NIVEL_BLITZ]-(User)-[r:APERTURA]->(Apertura) RETURN Apertura, count(r) AS num ORDER BY num desc
"""
