import math

class Geometria:
    
    def area_rectangulo(self, base, altura):
        return base * altura
    
    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)
    
    def area_circulo(self, radio):
        return math.pi * radio ** 2
    
    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio
    
    def area_triangulo(self, base, altura):
        return (base * altura) / 2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado, apotema):
        perimetro = self.perimetro_pentagono_regular(lado)
        return (perimetro * apotema) / 2
    
    def perimetro_pentagono_regular(self, lado):
        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        perimetro = self.perimetro_hexagono_regular(lado)
        return (perimetro * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
    
    def volumen_cubo(self, lado):
        return lado ** 3
    
    def area_superficie_cubo(self, lado):
        return 6 * (lado ** 2)
    
    def volumen_esfera(self, radio):
        return (4/3) * math.pi * (radio ** 3)
    
    def area_superficie_esfera(self, radio):
        return 4 * math.pi * (radio ** 2)
    
    def volumen_cilindro(self, radio, altura):
        return math.pi * (radio ** 2) * altura
    
    def area_superficie_cilindro(self, radio, altura):
        return 2 * math.pi * radio * (radio + altura)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            raise ValueError("La pendiente es indefinida (recta vertical).")
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        A = y1 - y2
        B = x2 - x1
        C = (x1 * y2) - (x2 * y1)
        return (A, B, C)
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        perimetro = self.perimetro_poligono_regular(num_lados, lado)
        return (perimetro * apotema) / 2
    
    def perimetro_poligono_regular(self, num_lados, lado):
        return num_lados * lado
    
def menu():
    geometria = Geometria()
    while True:
        print("\n ===== Menu de ecuaciones =====")
        print("1. Area de un rectangulo")
        print("2. Perimetro de un rectangulo")
        print("3. Area de un circulo")
        print("4. Perimetro de un circulo")
        print("5. Area de un triangulo")
        print("6. Perimetro de un triangulo")
        print("7. Validar triangulo")
        print("8. Area de un trapecio")
        print("9. Area de un rombo")
        print("10. Area de un pentagono regular")
        print("11. Perimetro de un pentagono regular")
        print("12. Area de un hexagono regular")
        print("13. Perimetro de un hexagono regular")
        print("14. Volumen de un cubo")
        print("15. Area de superficie de un cubo")
        print("16. Volumen de una esfera")
        print("17. Area de superficie de una esfera")
        print("18. Volumen de un cilindro")
        print("19. Area de superficie de un cilindro")
        print("20. Distancia entre dos puntos")
        print("21. Punto medio entre dos puntos")
        print("22. Pendiente de una recta")
        print("23. Ecuacion de una recta")
        print("24. Area de un poligono regular")
        print("25. Perimetro de un poligono regular")
        print("0. Salir")

        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            print("\n==================================\n")
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            resultado = geometria.area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "2":
            print("\n==================================\n")
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            resultado = geometria.perimetro_rectangulo(base, altura)
            print(f"El perímetro del rectángulo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "3":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio del círculo: "))
            resultado = geometria.area_circulo(radio)
            print(f"El área del círculo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "4":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio del círculo: "))
            resultado = geometria.perimetro_circulo(radio)
            print(f"El perímetro del círculo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "5":
            print("\n==================================\n")
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            resultado = geometria.area_triangulo(base, altura)
            print(f"El área del triángulo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "6":
            print("\n==================================\n")
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))
            resultado = geometria.perimetro_triangulo(lado1, lado2, lado3)
            print(f"El perímetro del triángulo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "7":
            print("\n==================================\n")
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))
            resultado = geometria.es_triangulo_valido(lado1, lado2, lado3)
            if resultado:
                print("Los lados forman un triángulo válido")
            else:
                print("Los lados NO forman un triángulo válido")
            print("\n==================================")
            
        elif opcion == "8":
            print("\n==================================\n")
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            resultado = geometria.area_trapecio(base_mayor, base_menor, altura)
            print(f"El área del trapecio es: {resultado}")
            print("\n==================================")
            
        elif opcion == "9":
            print("\n==================================\n")
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            resultado = geometria.area_rombo(diagonal_mayor, diagonal_menor)
            print(f"El área del rombo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "10":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del pentágono: "))
            apotema = float(input("Ingrese la apotema del pentágono: "))
            resultado = geometria.area_pentagono_regular(lado, apotema)
            print(f"El área del pentágono regular es: {resultado}")
            print("\n==================================")
            
        elif opcion == "11":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del pentágono: "))
            resultado = geometria.perimetro_pentagono_regular(lado)
            print(f"El perímetro del pentágono regular es: {resultado}")
            print("\n==================================")
            
        elif opcion == "12":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del hexágono: "))
            apotema = float(input("Ingrese la apotema del hexágono: "))
            resultado = geometria.area_hexagono_regular(lado, apotema)
            print(f"El área del hexágono regular es: {resultado}")
            print("\n==================================")
            
        elif opcion == "13":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del hexágono: "))
            resultado = geometria.perimetro_hexagono_regular(lado)
            print(f"El perímetro del hexágono regular es: {resultado}")
            print("\n==================================")
            
        elif opcion == "14":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del cubo: "))
            resultado = geometria.volumen_cubo(lado)
            print(f"El volumen del cubo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "15":
            print("\n==================================\n")
            lado = float(input("Ingrese el lado del cubo: "))
            resultado = geometria.area_superficie_cubo(lado)
            print(f"El área de superficie del cubo es: {resultado}")
            print("\n==================================")
            
        elif opcion == "16":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio de la esfera: "))
            resultado = geometria.volumen_esfera(radio)
            print(f"El volumen de la esfera es: {resultado}")
            print("\n==================================")
            
        elif opcion == "17":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio de la esfera: "))
            resultado = geometria.area_superficie_esfera(radio)
            print(f"El área de superficie de la esfera es: {resultado}")
            print("\n==================================")
            
        elif opcion == "18":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            resultado = geometria.volumen_cilindro(radio, altura)
            print(f"El volumen del cilindro es: {resultado}")
            print("\n==================================")
            
        elif opcion == "19":
            print("\n==================================\n")
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            resultado = geometria.area_superficie_cilindro(radio, altura)
            print(f"El área de superficie del cilindro es: {resultado}")
            print("\n==================================")
            
        elif opcion == "20":
            print("\n==================================\n")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            resultado = geometria.distancia_entre_puntos(x1, y1, x2, y2)
            print(f"La distancia entre los puntos es: {resultado}")
            print("\n==================================")
            
        elif opcion == "21":
            print("\n==================================\n")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            resultado = geometria.punto_medio(x1, y1, x2, y2)
            print(f"El punto medio es: ({resultado[0]}, {resultado[1]})")
            print("\n==================================")
            
        elif opcion == "22":
            print("\n==================================\n")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            try:
                resultado = geometria.pendiente_recta(x1, y1, x2, y2)
                print(f"La pendiente de la recta es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
            print("\n==================================")
            
        elif opcion == "23":
            print("\n==================================\n")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            resultado = geometria.ecuacion_recta(x1, y1, x2, y2)
            print(f"La ecuación de la recta es: {resultado[0]}x + {resultado[1]}y + {resultado[2]} = 0")
            print("\n==================================")
            
        elif opcion == "24":
            print("\n==================================\n")
            num_lados = int(input("Ingrese el número de lados del polígono: "))
            lado = float(input("Ingrese la longitud del lado: "))
            apotema = float(input("Ingrese la apotema del polígono: "))
            resultado = geometria.area_poligono_regular(num_lados, lado, apotema)
            print(f"El área del polígono regular es: {resultado}")
            print("\n==================================")
            
        elif opcion == "25":
            print("\n==================================\n")
            num_lados = int(input("Ingrese el número de lados del polígono: "))
            lado = float(input("Ingrese la longitud del lado: "))
            resultado = geometria.perimetro_poligono_regular(num_lados, lado)
            print(f"El perímetro del polígono regular es: {resultado}")
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