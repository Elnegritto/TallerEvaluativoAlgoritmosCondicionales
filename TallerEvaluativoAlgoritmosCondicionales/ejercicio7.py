#7. Diseñe un algoritmo que lea el nombre del estudiante, el valor de su matrícula en un curso que responda si¿ Es egresado de la universidad?, si la respuesta es SI, se le aplica un 30 % descuento. Muestre el nombre del estudiante y el valor de la matricula a pagar

name = input("Insert your name please: ")
value_registration = float(input("Enter the amount charged by the entity: "))
ask = input("Will he make it to graduate college?: ")
subDiscount = value_registration * 0.3
Discount = value_registration - subDiscount

if ask == "YES" or ask == "yes":
    print(f"\n\nName:{name}\nValue_registration: {Discount}")

else:
    print(f"\n\nName:{name}\nValue_registration: {value_registration}")