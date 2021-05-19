class Nodos:
    def __init__(self):
        self.nodos = []
        self.NIVEL = ["Principiante", "Intermedio", "Avanzado"]
        self.PARTE_FAVORITA = ["Apertura", "Medio", "Final"]
        self.PLATAFORMA = ["Chesscom", "Lichess", "Chess24"]
        self.APERTURA = ["Italiana_Espanola", "Inglesa", "Sistema_Londres", "Fianchetto"]
        self.DEFENSA = ["Eslava", "Francesa", "Caro_Kann", "Siciliana"]
        self.nodos.append(self.NIVEL)
        self.nodos.append(self.PARTE_FAVORITA)
        self.nodos.append(self.PLATAFORMA)
        self.nodos.append(self.APERTURA)
        self.nodos.append(self.DEFENSA)

    def creador_nodos_individuales(self, texto):
        texto_lower = texto.lower()
        texto_capitalizado = texto.capitalize()
        comando = f"({texto_lower}:{texto_capitalizado} {{nombre:\"{texto}\"}})"
        return comando

    def creador_nodos(self):
        comando_nodos = "CREATE \n"
        for lista in self.nodos:
            for elemento in lista:
                comando_nodos += self.creador_nodos_individuales(elemento) + ",\n"
        return comando_nodos[:-2]

print(Nodos().creador_nodos())
