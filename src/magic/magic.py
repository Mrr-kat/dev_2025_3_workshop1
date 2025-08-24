class Magic:
    
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n+1):
                a, b = b, a + b
            return b
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        secuencia = [0, 1]
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]
    
    def es_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [i for i in range(2, n+1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        triangulo = [[1]]
        for _ in range(1, filas):
            fila_anterior = triangulo[-1]
            fila = [1]
            for j in range(len(fila_anterior) - 1):
                fila.append(fila_anterior[j] + fila_anterior[j+1])
            fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a*b) // self.mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d)**potencia for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        if not matriz or any(len(fila) != len(matriz) for fila in matriz):
            return False
        n = len(matriz)
        suma_ref = sum(matriz[0])
        

        for i in range(n):
            if sum(matriz[i]) != suma_ref or sum(matriz[j][i] for j in range(n)) != suma_ref:
                return False
        

        if sum(matriz[i][i] for i in range(n)) != suma_ref:
            return False
        if sum(matriz[i][n-i-1] for i in range(n)) != suma_ref:
            return False
        
        return True




def menu():
    m = Magic()
    
    while True:
        print("\n===== Menu magico =====")
        print("1. Fibonacci")
        print("2. Secuencia Fibonacci")
        print("3. Verificar número primo")
        print("4. Generar números primos hasta n")
        print("5. Verificar número perfecto")
        print("6. Triángulo de Pascal")
        print("7. Factorial")
        print("8. Máximo Común Divisor (MCD)")
        print("9. Mínimo Común Múltiplo (MCM)")
        print("10. Suma de dígitos")
        print("11. Verificar número Armstrong")
        print("12. Verificar cuadrado mágico")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n==================================\n")
            n = int(input("Ingrese n: "))
            print("Fibonacci:", m.fibonacci(n))
            print("\n==================================")

        elif opcion == "2":
            print("\n==================================\n")
            n = int(input("Ingrese cantidad de términos: "))
            print("Secuencia Fibonacci:", m.secuencia_fibonacci(n))
            print("\n==================================")

        elif opcion == "3":
            print("\n==================================\n")
            n = int(input("Ingrese un número: "))
            print("¿Es primo?", m.es_primo(n))
            print("\n==================================")

        elif opcion == "4":
            print("\n==================================\n")
            n = int(input("Generar primos hasta: "))
            print("Primos:", m.generar_primos(n))
            print("\n==================================")

        elif opcion == "5":
            print("\n==================================\n")
            n = int(input("Ingrese un número: "))
            print("¿Es número perfecto?", m.es_numero_perfecto(n))
            print("\n==================================")

        elif opcion == "6":
            print("\n==================================\n")
            filas = int(input("Ingrese número de filas: "))
            for fila in m.triangulo_pascal(filas):
                print(fila)
            print("\n==================================")

        elif opcion == "7":
            print("\n==================================\n")
            n = int(input("Ingrese un número: "))
            print("Factorial:", m.factorial(n))
            print("\n==================================")

        elif opcion == "8":
            print("\n==================================\n")
            a = int(input("Ingrese primer número: "))
            b = int(input("Ingrese segundo número: "))
            print("MCD:", m.mcd(a, b))
            print("\n==================================")

        elif opcion == "9":
            print("\n==================================\n")
            a = int(input("Ingrese primer número: "))
            b = int(input("Ingrese segundo número: "))
            print("MCM:", m.mcm(a, b))
            print("\n==================================")

        elif opcion == "10":
            print("\n==================================\n")
            n = int(input("Ingrese un número: "))
            print("Suma de dígitos:", m.suma_digitos(n))
            print("\n==================================")

        elif opcion == "11":
            print("\n==================================\n")
            n = int(input("Ingrese un número: "))
            print("¿Es número Armstrong?", m.es_numero_armstrong(n))
            print("\n==================================")

        elif opcion == "12":
            print("\n==================================\n")
            n = int(input("Ingrese tamaño de la matriz (n x n): "))
            matriz = []
            for i in range(n):
                fila = list(map(int, input(f"Fila {i+1} (separar con espacios): ").split()))
                matriz.append(fila)
            print("¿Es cuadrado mágico?", m.es_cuadrado_magico(matriz))
            print("\n==================================")

        elif opcion == "0":
            print("\n==================================\n")
            print("¡Hasta luego!")
            print("\n==================================")
            break
        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "_main_":
    menu()