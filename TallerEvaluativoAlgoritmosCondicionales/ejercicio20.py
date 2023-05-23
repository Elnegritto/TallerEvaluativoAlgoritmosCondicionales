#20. Algoritmo para hallar el área de un cuadrado si el valor del lado es mayor a 10, de lo contrario generar un mensaje de “no aplica”.

value1 = int(input("Type one side: "))
value2 = int(input("Type the other side: "))
area = value1 * value2

if area > 10:
    print(f"The area is {area}")
    
else:
    print("Does not apply this procedure")