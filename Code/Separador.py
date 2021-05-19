class Separador:
    def __init__(self, texto):
        self.separado = texto.split(",")

    @property
    def retonar(self):
        USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA = self.separado
        Nodo_NIVEL_BLITZ =f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:NIVEL_BLITZ]->({NIVEL_BLITZ.lower()})"
        Nodo_NIVEL_RAPIDAS = f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:NIVEL_RAPIDAS]->({NIVEL_RAPIDAS.lower()})"
        Nodo_PARTE_FAVORITA = f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:PARTE_FAVORITA]->({PARTE_FAVORITA.lower()})"
        Nodo_PLATAFORMA = f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:PLATAFORMA]->({PLATAFORMA.lower()})"
        Nodo_APERTURA = f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:APERTURA]->({APERTURA.lower()})"
        Nodo_DEFENSA = f"MATCH {USER}:{USER.capitalize()} MERGE ({USER})-[:DEFENSA]->({DEFENSA.lower()})"
        Connection = Nodo_NIVEL_BLITZ +";\n"+Nodo_NIVEL_RAPIDAS +";\n"+  Nodo_PARTE_FAVORITA +";\n"+  Nodo_PLATAFORMA +";\n"+Nodo_APERTURA +";\n"+ Nodo_DEFENSA
        return Connection
