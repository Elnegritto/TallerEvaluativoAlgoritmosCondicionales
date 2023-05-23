#17. Hacer un programa que pida dos números y los imprima en forma ascendente y descendente.

list = []
value1 = int(input("Type a number "))
value2 = int(input("Enter another number please: "))

list.append(value1)
list.append(value2)

print(f"\nThe numbers to be added are: {value1} and {value2}")

list.sort()

print(f"\nAscending List: {list}")

list.reverse()

print(f"\nDescending List: {list}")
