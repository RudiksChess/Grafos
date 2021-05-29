ans=True

while ans:
    print("""
        |-----------------------------------CLUB DE AJEDREZ -----------------------------------|
        |______________________________SISTEMA DE RECOMENDACIONES______________________________|
        Seleccionar una opción: 
        1. Entrar al sistema de recomendaciones.
        2. Configuraciones (solo administradores).
        3. Salir. 
        """)
    ans=int(input("Opción:"))
    if ans==1:
        print("""----------------------RESPONDER------------------------------""")
        print("""¿Nivel de blitz? Considere: 
                 1. Principiante [0-1400]
                 2. Intermedio [1400-1600]
                 3. Avanzado [1600-infinito]
                 """)
        blitz= int(input("NIVEL_BLITZ: "))
        print("""¿Nivel de rápidas? Considere: 
                         1. Principiante [0-1400]
                         2. Intermedio [1400-1600]
                         3. Avanzado [1600-infinito]
                         """)
        rapidas = int(input("NIVEL_RÁPIDAS: "))

    elif ans==2:
      print(""" ------------- CONFIGURACIONES --------------
      Seleccionar una opción: 
      1. Agregar a un usuario.
      2. Borrar a un usuario. 
      """)
      configuraciones = int(input("Opción"))
      if configuraciones == 1:
          print("----Datos del usuario-----")
          nivel_blitz = str(input("NIVEL_BLITZ:"))
          nivel_rapidas = str(input("NIVEL_RAPIDAS:"))
          parte_favorita = str(input("PARTE_FAVORITA:"))
          plataforma = str(input("PLATAFORMA:"))
          apertura = str(input("APERTURA:"))
          defensa = str(input("DEFENSA:"))
          print("Usuario creado.")
      elif configuraciones ==2:
          id = str(input("¿Cuál es el ID del usuario?"))
          print("Usuario borrado.")

    else:
        print("Programa cerrado. Base de datos borrada.")
