import Code.Separador as separador
with open("Datos.csv") as f:
    lis = [line.split() for line in f]
    lis.pop(0)
    for elemento in lis[0:1]:
        Nodo_NIVEL_BLITZ, Nodo_NIVEL_RAPIDAS, Nodo_PARTE_FAVORITA, Nodo_PLATAFORMA, Nodo_APERTURA, Nodo_DEFENSA = \
            separador.Separador(elemento[0]).retonar

