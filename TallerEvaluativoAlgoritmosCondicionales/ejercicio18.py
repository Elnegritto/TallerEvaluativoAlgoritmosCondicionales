#18. Hacer un programa que pida 3 números e indicar si el tercero es igual a la suma del primero y el segundo.

number1 = int(input("Type a number : "))
number2 = int(input("Enter another number please: "))
number3 = int(input("Enter another number please: "))
sum = number1 + number2

if number3 == sum:
    print(f"The sum {number1} and {number2} is equal {number3}")
    
else:
    print(f"the sum of numbers {number1} and {number2} do not equal {number3}")