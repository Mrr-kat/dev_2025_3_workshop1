class Data:
   
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
            
    def eliminar_duplicados(self, lista):
        resultado = []
        for elem in lista:
            if elem not in resultado:
                resultado.append(elem)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = 0
        for num in lista:
            suma_real += num
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        def push(x): pila.append(x)
        def pop(): return pila.pop() if pila else None
        def peek(): return pila[-1] if pila else None
        def is_empty(): return len(pila) == 0
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
    
    def implementar_cola(self):
        cola = []
        def enqueue(x): cola.append(x)
        def dequeue(): return cola.pop(0) if cola else None
        def peek(): return cola[0] if cola else None
        def is_empty(): return len(cola) == 0
        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
    
    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)
        return transpuesta



def menu():
    data = Data()
    
    while True:
        print("\n ===== Menu de funciones =====")
        print("1. Invertir lista")
        print("2. Buscar elemento en lista")
        print("3. Eliminar duplicados de una lista")
        print("4. Merge de listas ordenadas")
        print("5. Rotar lista")
        print("6. Encontrar número faltante")
        print("7. Verificar subconjunto")
        print("8. Usar pila")
        print("9. Usar cola")
        print("10. Transponer matriz")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opcion: ")
        
        if opcion == "1":
            print("\n==================================\n")
            lista = input("Ingresa lista separada por comas: ").split(",")
            print("Invertida:", data.invertir_lista(lista))
            print("\n==================================")
        
        elif opcion == "2":
            print("\n==================================\n")
            lista = input("Ingresa lista separada por comas: ").split(",")
            elemento = input("Elemento a buscar: ")
            print("Índice:", data.buscar_elemento(lista, elemento))
            print("\n==================================")
        
        elif opcion == "3":
            print("\n==================================\n")
            lista = input("Ingresa lista separada por comas: ").split(",")
            print("Sin duplicados:", data.eliminar_duplicados(lista))
            print("\n==================================")
        
        elif opcion == "4":
            print("\n==================================\n")
            lista1 = input("Lista 1 ordenada (comas): ").split(",")
            lista2 = input("Lista 2 ordenada (comas): ").split(",")
            print("Merge ordenado:", data.merge_ordenado(lista1, lista2))
            print("\n==================================")
        
        elif opcion == "5":
            print("\n==================================\n")
            lista = input("Ingresa lista separada por comas: ").split(",")
            k = int(input("Número de rotaciones: "))
            print("Rotada:", data.rotar_lista(lista, k))
            print("\n==================================")
        
        elif opcion == "6":
            print("\n==================================\n")
            lista = list(map(int, input("Ingresa lista de enteros (1 a n) separada por comas: ").split(",")))
            print("Número faltante:", data.encuentra_numero_faltante(lista))
            print("\n==================================")
        
        elif opcion == "7":
            print("\n==================================\n")
            conjunto1 = input("Conjunto 1 (comas): ").split(",")
            conjunto2 = input("Conjunto 2 (comas): ").split(",")
            print("¿Es subconjunto?:", data.es_subconjunto(conjunto1, conjunto2))
            print("\n==================================")
        
        elif opcion == "8":
            print("\n==================================\n")
            pila = data.implementar_pila()
            pila["push"]("A")
            pila["push"]("B")
            print("Peek:", pila["peek"]())
            print("Pop:", pila["pop"]())
            print("¿Está vacía?:", pila["is_empty"]())
            print("\n==================================")
        
        elif opcion == "9":
            print("\n==================================\n")
            cola = data.implementar_cola()
            cola["enqueue"]("A")
            cola["enqueue"]("B")
            print("Peek:", cola["peek"]())
            print("Dequeue:", cola["dequeue"]())
            print("¿Está vacía?:", cola["is_empty"]())
            print("\n==================================")
        
        elif opcion == "10":
            print("\n==================================\n")
            filas = int(input("Número de filas: "))
            matriz = []
            for i in range(filas):
                fila = input(f"Fila {i+1} (comas): ").split(",")
                matriz.append(fila)
            print("Transpuesta:", data.matriz_transpuesta(matriz))
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