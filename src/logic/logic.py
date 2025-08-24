class Logica:
    
    def AND(self, a, b):
        return a and b
    
    def OR(self, a, b):
        return a or b
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return (a and not b) or (not a and b)
    
    def NAND(self, a, b):
        return not (a and b)
    
    def NOR(self, a, b):
        return not (a or b)
    
    def XNOR(self, a, b):
        return not ((a and not b) or (not a and b))
    
    def implicacion(self, a, b):
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        return a == b

def menu():
    logica = Logica()
    while True:
        print("\n ===== Menu de Lógica Proposicional =====")
        print("1. AND")
        print("2. OR ")
        print("3. NOT ")
        print("4. XOR ")
        print("5. NAND ")
        print("6. NOR ")
        print("7. XNOR ")
        print("8. Implicación ")
        print("9. Bi-implicación ")
        print("0. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.AND(a, b)
            print(f"a AND b: {resultado}")
            print("\n==================================")
            
        elif opcion == "2":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.OR(a, b)
            print(f"a OR b: {resultado}")
            print("\n==================================")
            
        elif opcion == "3":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.NOT(a)
            print(f"NOT a: {resultado}")
            print("\n==================================")
            
        elif opcion == "4":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.XOR(a, b)
            print(f"a XOR b: {resultado}")
            print("\n==================================")
            
        elif opcion == "5":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.NAND(a, b)
            print(f"a NAND b: {resultado}")
            print("\n==================================")
            
        elif opcion == "6":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.NOR(a, b)
            print(f"a NOR b: {resultado}")
            print("\n==================================")
            
        elif opcion == "7":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.XNOR(a, b)
            print(f"a XNOR b: {resultado}")
            print("\n==================================")
            
        elif opcion == "8":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.implicacion(a, b)
            print(f"a → b: {resultado}")
            print("\n==================================")
            
        elif opcion == "9":
            print("\n==================================\n")
            a = input("Ingrese True/False para a (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            b = input("Ingrese True/False para b (1/True, 0/False): ").lower() in ('true', '1', 't', 'yes', 'y')
            resultado = logica.bi_implicacion(a, b)
            print(f"a ↔ b: {resultado}")
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