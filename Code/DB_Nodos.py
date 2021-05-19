def creador_nodos_individuales(texto):
    texto_lower = texto.lower()
    texto_capitalizado = texto.capitalize()
    comando = f"({texto_lower}:{texto_capitalizado} {{nombre:\"{texto}\"}})"
    return comando

class Nodos:
    def __init__(self):
        self.nodos = []
        self.users = ["user001","user002","user003","user004","user005","user006","user007","user008","user009", "user010",
                     "user011", "user012", "user013", "user014", "user015", "user016", "user017", "user018", "user019", "user020",
                     "user021", "user022", "user023", "user024"]
        self.NIVEL = ["Principiante", "Intermedio", "Avanzado"]
        self.PARTE_FAVORITA = ["Apertura", "Medio", "Final"]
        self.PLATAFORMA = ["Chesscom", "Lichess", "Chess24"]
        self.APERTURA = ["Italiana_Espanola", "Inglesa", "Sistema_Londres", "Fianchetto"]
        self.DEFENSA = ["Eslava", "Francesa", "Caro_Kann", "Siciliana"]
        self.nodos.append(self.users)
        self.nodos.append(self.NIVEL)
        self.nodos.append(self.PARTE_FAVORITA)
        self.nodos.append(self.PLATAFORMA)
        self.nodos.append(self.APERTURA)
        self.nodos.append(self.DEFENSA)

    @property
    def creador_nodos(self):
        comando_nodos: str = "CREATE \n"
        for lista in self.nodos:
            for elemento in lista:
                comando_nodos += creador_nodos_individuales(elemento) + ",\n"
        return comando_nodos[:-2]


print(Nodos().creador_nodos)
