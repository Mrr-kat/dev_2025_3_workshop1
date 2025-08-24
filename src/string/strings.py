class Strings:
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]

    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida

    def contar_vocales(self, texto):
        vocales = "aeiouáéíóú"
        contador = 0
        for char in texto.lower():
            if char in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        vocales = "aeiouáéíóú"
        contador = 0
        for char in texto.lower():
            if char.isalpha() and char not in vocales:
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)

    def palabras_mayus(self, texto):
        palabras = texto.split()
        return " ".join([p.capitalize() for p in palabras])

    def eliminar_espacios_duplicados(self, texto):
        palabras = texto.split()
        return " ".join(palabras)

    def es_numero_entero(self, texto):
        if texto.startswith("-"):
            texto = texto[1:]
        if not texto:
            return False
        for char in texto:
            if char < "0" or char > "9":
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones



def menu():
    strings = Strings()

    while True:
        print("\n ===== Menu de funciones clase str =====")
        print("1. Verificar si es palíndromo")
        print("2. Invertir cadena")
        print("3. Contar vocales")
        print("4. Contar consonantes")
        print("5. Verificar anagrama")
        print("6. Contar palabras")
        print("7. Poner en mayúscula la primera letra de cada palabra")
        print("8. Eliminar espacios duplicados")
        print("9. Verificar si es número entero")
        print("10. Cifrar con César")
        print("11. Descifrar con César")
        print("12. Encontrar subcadena")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("¿Es palíndromo?:", strings.es_palindromo(texto))
            print("\n==================================")

        elif opcion == "2":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Invertida:", strings.invertir_cadena(texto))
            print("\n==================================")

        elif opcion == "3":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Número de vocales:", strings.contar_vocales(texto))
            print("\n==================================")

        elif opcion == "4":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Número de consonantes:", strings.contar_consonantes(texto))
            print("\n==================================")

        elif opcion == "5":
            print("\n==================================\n")
            t1 = input("Ingrese primer texto: ")
            t2 = input("Ingrese segundo texto: ")
            print("¿Son anagramas?:", strings.es_anagrama(t1, t2))
            print("\n==================================")

        elif opcion == "6":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Número de palabras:", strings.contar_palabras(texto))
            print("\n==================================")

        elif opcion == "7":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Texto transformado:", strings.palabras_mayus(texto))
            print("\n==================================")

        elif opcion == "8":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("Texto sin espacios duplicados:", strings.eliminar_espacios_duplicados(texto))
            print("\n==================================")

        elif opcion == "9":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            print("¿Es número entero?:", strings.es_numero_entero(texto))
            print("\n==================================")

        elif opcion == "10":
            print("\n==================================\n")
            texto = input("Ingrese un texto: ")
            desplazamiento = int(input("Ingrese desplazamiento: "))
            print("Texto cifrado:", strings.cifrar_cesar(texto, desplazamiento))
            print("\n==================================")

        elif opcion == "11":
            print("\n==================================\n")
            texto = input("Ingrese un texto cifrado: ")
            desplazamiento = int(input("Ingrese desplazamiento usado: "))
            print("Texto descifrado:", strings.descifrar_cesar(texto, desplazamiento))
            print("\n==================================")

        elif opcion == "12":
            print("\n==================================\n")
            texto = input("Ingrese el texto: ")
            subcadena = input("Ingrese la subcadena: ")
            print("Posiciones encontradas:", strings.encontrar_subcadena(texto, subcadena))
            print("\n==================================")

        elif opcion == "0":
            print("\n==================================\n")
            print("¡Hasta luego!")
            print("\n==================================")
            break

        else:
            print("Opción no válida, intente de nuevo.")



if __name__ == "_main_":
    menu()