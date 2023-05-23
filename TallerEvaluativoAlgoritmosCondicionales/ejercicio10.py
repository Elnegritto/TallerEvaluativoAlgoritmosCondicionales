#10. Mostrar la suma de dos números enteros, si el resultado supera a 10.

number1 = int(input("Enter a number please: "))
number2 = int(input("Enter another number please: "))
sum = number1 + number2

if sum >= 10:
    print(f"the sum of the numbers gives as a result: {sum}")
    
else:
    print("\nthe sum of these numbers did not reach the minimum requirement to make said sum.")