#1. Diseñe un algoritmo que capture dos números, y que realice la suma de dichos números, y mostrar los datos si es el resultado no es negativo.

number1 = float(input("Type a number : "))
number2 = float(input("Enter a second number : "))
suma = number1+number2

if suma > 0:
    print(f"The sum results in : {suma}")
    
else:
    print(f"The sum you entered is negative")