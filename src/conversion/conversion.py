class Conversion:
    def celsius_a_fahrenheit(self):
        print("\n==================================")
        celsius = float(input("Ingrese la temperaura en grados celcius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}C equivalen a {fahrenheit}F")
        print("==================================")
    
    def fahrenheit_a_celsius(self):
        print("\n==================================")
        fahrenheit =float(input("Ingrese la temperatura en grados faherenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}F equivalen a {celsius}C")
        print("==================================")
    
    def metros_a_pies(self):
        print("\n==================================")
        metros = float(input("Ingrese la cantidad de metros: "))
        pies = metros * 3.28084
        print(f"{metros} metros equivalen a {pies} pies")
        print("==================================")


    def pies_a_metros(self):
        print("\n==================================")
        pies=float(input("Ingrese la distancia en pies: "))
        metros = pies / 3.28084
        print(f"{pies} pies equivalen a {metros} metros")
        print("==================================")
    

    def decimal_a_binario(self):
        print("\n==================================")
        decimal = int(input("Ingrese un numero entero: "))
        binario = bin(decimal)[2:]
        print(f"{decimal} en decimal, es {binario} en binario")
        print("==================================")
        
    
    def binario_a_decimal(self):
        print("\n==================================")
        binario = str(input("Ingrese un numero binario: "))
        decimal = int(binario, 2)
        print(f"{binario} en binario, es {decimal} en decimal")
        print("==================================")

    def decimal_a_romano(self):
        print("\n==================================")
        numero = int(input("Ingrese un numero entero: "))
        if numero < 1 or numero > 3999:
            print("El numero debe estar entre 1 y 3999")
        else:
            romano = self.convierte_a_romano(numero)
            print(f"{numero} en decimal, es {romano} en romano")
        print("==================================")

    def convierte_a_romano(self, numero):
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def romano_a_decimal(self):
        print("\n==================================")
        romano = input("Ingrese un número en romano: ").upper()
        valores = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        i = 0
        while i < len(romano):
            if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                total += valores[romano[i+1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        print(f"{romano} en romano, es {total} en decimal")
        print("==================================")
        return total

    def texto_a_morse(self):
        print("\n==================================")
        texto = input("Ingrese un texto: ").upper()
        morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }
        texto = texto.upper()
        morse = " ".join(morse_dict[c] for c in texto if c in morse_dict)
        print(f"{texto} en texto, es {morse} en Morse")
        print("==================================")
        return morse

    def morse_a_texto(self):
        print("\n==================================")
        morse = input("Ingrese código morse: ")
        morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }
        inv_morse_dict = {v: k for k, v in morse_dict.items()}
        texto = "".join(inv_morse_dict[c] for c in morse.split() if c in inv_morse_dict)
        print(f"{morse} en Morse, es {texto} en texto")
        print("==================================")
    
    def menu(self):
        while True:
            print("\n --- conversor ---")
            print("1. convertir de celsius a fahrenheit")
            print("2. convertir de fahrenheit a celsius")
            print("3. convertir de metros a pies")
            print("4. convertir de pies a metros")
            print("5. convertir de decimal a binario")
            print("6. convertir de binario a decimal")
            print("7. convertir de decimal a romano")
            print("8. convertir de romano a decimal")
            print("9. convertir de texto a morse")
            print("10. convertir de morse a texto")
            print("11. convertir de morse a texto")

            opcion = input("\nIngrese una opcion: ")

            if(opcion == "1"):
                self.celsius_a_fahrenheit()
            elif(opcion == "2"):
                self.fahrenheit_a_celsius()
            elif(opcion == "3"):
                self.metros_a_pies()
            elif(opcion == "4"):
                self.pies_a_metros()
            elif(opcion == "5"):
                self.decimal_a_binario()
            elif(opcion == "6"):
                self.binario_a_decimal()
            elif(opcion == "7"):
                self.decimal_a_romano()
            elif(opcion == "8"):
                self.romano_a_decimal()
            elif(opcion == "9"):
                self.texto_a_morse()
            elif(opcion == "10"):
                self.morse_a_texto()
            elif(opcion == "0"):
                print("¡Hasta luego!")
                break
            else:
                print("Opcion no valida")


if __name__ == "__main__":
    app = Conversion()
    app.menu()