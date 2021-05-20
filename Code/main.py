from neo4j import GraphDatabase, WRITE_ACCESS
import Code.Separador as separador
import Code.DB_Nodos as nodos


class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def base(self):
        session = self.driver.session(default_access_mode=WRITE_ACCESS)
        noditos = nodos.Nodos().creador_nodos
        session.run(noditos)
        with open("Datos.csv") as f:
            lis = [line.split() for line in f]
            lis.pop(0)
            for elemento in lis:
                Nodo_NIVEL_BLITZ,Nodo_NIVEL_RAPIDAS,Nodo_PARTE_FAVORITA, Nodo_PLATAFORMA,Nodo_APERTURA,Nodo_DEFENSA = \
                    separador.Separador(elemento[0]).retonar
                session.run(Nodo_NIVEL_BLITZ)
                session.run(Nodo_NIVEL_RAPIDAS)
                session.run(Nodo_PARTE_FAVORITA)
                session.run(Nodo_PLATAFORMA)
                session.run(Nodo_APERTURA)
                session.run(Nodo_DEFENSA)
        session.run(Nodo_DEFENSA)
        session.close()



    def close(self):
        self.driver.close()



if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:11003", "neo4j", "12345")
    greeter.base()
    greeter.close()
