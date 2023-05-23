#9. Determinar si un aprendiz aprueba o reprueba una formación, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 10; reprueba en caso contrario

name = input("Enter your name please: ")
formation = input("Enter the name of your training: ")
note1 = int(input("Insert note 1: "))
note2 = int(input("Insert note 2: "))
note3 = int(input("Insert note 3: "))
average = (note1 + note2 + note3)/3

if average >= 10:
    print("congratulations you have passed the training")
    
else:
    print("unfortunately you have not passed the training")
