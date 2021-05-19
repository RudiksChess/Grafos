class Separador:
    def __init__(self, texto):
        self.separado = texto.split(",")

    @property
    def retonar(self):
        USER, NIVEL_BLITZ, NIVEL_RAPIDAS, PARTE_FAVORITA, PLATAFORMA, APERTURA, DEFENSA = self.separado
        return USER


print(Separador("user001,Principiante,Intermedio,Medio,Chess.com,Inglesa,Siciliana").retonar)
