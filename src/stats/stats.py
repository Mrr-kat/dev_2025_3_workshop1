class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        numeros = sorted(numeros)
        n = len(numeros)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros[mitad - 1] + numeros[mitad]) / 2
        else:
            return numeros[mitad]

    def moda(self, numeros):
        conteos = {}
        for num in numeros:
            conteos[num] = conteos.get(num, 0) + 1
        return max(conteos, key=conteos.get)

    def desviacion_estandar(self, numeros):
        media = self.promedio(numeros)
        suma = sum((x - media) ** 2 for x in numeros)
        return (suma / len(numeros)) ** 0.5

    def varianza(self, numeros):
        media = self.promedio(numeros)
        suma = sum((x - media) ** 2 for x in numeros)
        return suma / len(numeros)

    def rango(self, numeros):
        return max(numeros) - min(numeros)

def convertir_lista_numeros(entrada):
    str_a_int = [float(x.strip()) for x in entrada.split(",")]
    return str_a_int

def menu():
    stats = Stats()
    while True:
        print("\n ===== Menu de Estadísticas =====")
        print("1. Promedio (Media)")
        print("2. Mediana")
        print("3. Moda")
        print("4. Desviación Estándar")
        print("5. Varianza")
        print("6. Rango")
        print("0. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Promedio: ", stats.promedio(numeros))
            print("\n==================================")
            
        elif opcion == "2":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Mediana: ", stats.mediana(numeros))
            print("\n==================================")
            
        elif opcion == "3":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Moda: ", stats.moda(numeros))
            print("\n==================================")
            
        elif opcion == "4":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Desviación Estándar: ", stats.desviacion_estandar(numeros))
            print("\n==================================")
            
        elif opcion == "5":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Varianza: ", stats.varianza(numeros))
            print("\n==================================")
            
        elif opcion == "6":
            print("\n==================================\n")
            entrada = input("Ingrese números separados por comas: ")
            numeros = convertir_lista_numeros(entrada)
            print("Rango: ", stats.rango(numeros))
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