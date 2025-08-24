import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        reglas = {
            "piedra": "tijera",  
            "tijera": "papel",   
            "papel": "piedra"    
        }
        
        if jugador1 == jugador2:
            return "empate"
        elif reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto):
        while True:
            intento = int(input("Ingrese su intento: "))
            if intento == numero_secreto:
                print("correcto")
                break
            elif intento > numero_secreto:
                print("muy alto")
            else:
                print("muy bajo")
    
    def ta_te_ti_ganador(self, tablero):
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return tablero[0][i]

        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        elif desde_fila == hasta_fila:  
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False
        else:  
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False
        return True



def menu():
    games = Games()
    while True:
        print("\n ===== Menu de juegos =====")
        print("1. Piedra, Papel o Tijera")
        print("2. Adivinar numero con pista")
        print("3. Ta-Te-Ti (Tic-Tac-Toe)")
        print("4. Generar combinación mastermind")
        print("5. Validar movimiento de torre en ajedrez")
        print("0. Salir")

        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            print("\n==================================\n")
            jugador1 = input("Jugador 1, ingreser piedra, papel o tijera: ").lower()
            jugador2 = input("Jugador 2, ingrese piedra, papel o tijera: ").lower()
            print("Resultado:", games.piedra_papel_tijera(jugador1, jugador2))
            print("\n==================================")

        elif opcion == "2":
            print("\n==================================\n")
            numero_secreto = int(input("Ingrese el numero secreto: "))
            games.adivinar_numero_pista(numero_secreto)
            print("\n==================================")

        elif opcion == "3":
            print("\n==================================\n")
            print("Ingrese el tablero, 3 filas con valores X, O o espacio ' ', separado por comas")
            tablero = []
            for i in range(3):
                fila = input(f"Fila {i+1} (ejemplo: X,O, ): ").split(",")
                tablero.append(fila)
            print("Resultado:", games.ta_te_ti_ganador(tablero))
            print("\n==================================")

        elif opcion == "4":
            print("\n==================================\n")
            colores = input("Colores disponibles (separados por comas): ").split(",")
            longitud = int(input("Longitud de la combinación: "))
            print("Combinación generada:", games.generar_combinacion_mastermind(longitud, colores))
            print("\n==================================")

        elif opcion == "5":
            print("\n==================================\n")
            print("Tablero de ajedrez vacío (8x8, espacios en blanco).")
            tablero = [[" " for _ in range(8)] for _ in range(8)]
            desde_fila = int(input("Fila inicial (0-7): "))
            desde_col = int(input("Columna inicial (0-7): "))
            hasta_fila = int(input("Fila destino (0-7): "))
            hasta_col = int(input("Columna destino (0-7): "))
            print("Movimiento válido:", games.validar_movimiento_torre_ajedrez(desde_fila, desde_col, hasta_fila, hasta_col, tablero))
            print("\n==================================")

        elif opcion == "0":
            print("\n==================================\n")
            print("¡Hasta luego!")
            print("\n==================================")
            break
        

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
