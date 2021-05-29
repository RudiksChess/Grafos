from neo4j import GraphDatabase, WRITE_ACCESS
import Code.DB_Nodos as nodos


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



    def close(self):
        self.driver.close()



if __name__ == "__main__":
    greeter = DB("bolt://localhost:11006", "neo4j", "12345")
    greeter.base()
    greeter.close()

"""
MATCH (nodo:Nivel {nombre:"principiante"})<-[:NIVEL_BLITZ]-(User)-[r:APERTURA]->(Apertura) RETURN Apertura, count(r) AS num ORDER BY num desc
"""