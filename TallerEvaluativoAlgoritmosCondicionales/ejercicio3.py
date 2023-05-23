#3. Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso, nota definitiva, el nro de clases en el semestre y el número de las fallas. En el caso de que las fallas superen el 30% del número de clases se debe mostrar la nota que no aprobó y se calificara cero(0).

name = input("Enter your name: ")
name_curse = input("Enter the name of the course: ")
note = float(input("Enter your final grade: "))
number_of_classes = int(input("Enter the number of classes seen in the semester: "))
number_of_failures = int(input("Enter your number of failures: "))
note = number_of_classes * 0.3

if number_of_failures <= note:
    print(f"\n\nInformation of your current semester: \nName: {name}\nCurse: {name_curse}\nN. Classes: {number_of_classes}\nN. Fails: {number_of_failures}")
    
else:
    note = 0
    print(f"\n\nInformation of your current semester: \nName: {name}\nCurse: {name_curse}\nN. Classes: {number_of_classes}\nN. Fails: {number_of_failures}")     
