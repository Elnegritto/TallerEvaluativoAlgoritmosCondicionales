#14. Un trabajador necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: si trabaja 20 horas o menos se le paga $10.000 por hora; si trabaja más de 20 horas se le paga $35.000 por hora.

name = input("write your name: ")
hours = int(input("enter the number of hours you work: "))

if hours >= 30:
    salary1 = hours * 35000
    print(f"his salary is as follows: {salary1}")
    
else:
    salary2 = hours * 10000
    print(f"his salary is as follows: {salary2}")