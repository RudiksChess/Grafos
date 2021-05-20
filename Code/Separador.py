class Separador:
    def __init__(self, texto):
        self.separado = texto.split(",")

    @property
    def retonar(self):
        USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA = self.separado
        Nodo_NIVEL_BLITZ =f"MATCH ({USER}:{USER.capitalize()}), ({NIVEL_BLITZ.lower()}:{NIVEL_BLITZ.capitalize()}) MERGE ({USER})-[:NIVEL_BLITZ]->({NIVEL_BLITZ.lower()})"
        Nodo_NIVEL_RAPIDAS = f"MATCH ({USER}:{USER.capitalize()}), ({NIVEL_RAPIDAS.lower()}:{NIVEL_RAPIDAS.capitalize()}) MERGE ({USER})-[:NIVEL_RAPIDAS]->({NIVEL_RAPIDAS.lower()})"
        Nodo_PARTE_FAVORITA = f"MATCH ({USER}:{USER.capitalize()}),({PARTE_FAVORITA.lower()}:{PARTE_FAVORITA.capitalize()}) MERGE ({USER})-[:PARTE_FAVORITA]->({PARTE_FAVORITA.lower()})"
        Nodo_PLATAFORMA = f"MATCH ({USER}:{USER.capitalize()}),({PLATAFORMA.lower()}:{PLATAFORMA.capitalize()}) MERGE ({USER})-[:PLATAFORMA]->({PLATAFORMA.lower()})"
        Nodo_APERTURA = f"MATCH ({USER}:{USER.capitalize()}), ({APERTURA.lower()}:{APERTURA.capitalize()}) MERGE ({USER})-[:APERTURA]->({APERTURA.lower()})"
        Nodo_DEFENSA = f"MATCH ({USER}:{USER.capitalize()}), ({DEFENSA.lower()}:{DEFENSA.capitalize()}) MERGE ({USER})-[:DEFENSA]->({DEFENSA.lower()})"

        return Nodo_NIVEL_BLITZ,Nodo_NIVEL_RAPIDAS,Nodo_PARTE_FAVORITA, Nodo_PLATAFORMA,Nodo_APERTURA,Nodo_DEFENSA

