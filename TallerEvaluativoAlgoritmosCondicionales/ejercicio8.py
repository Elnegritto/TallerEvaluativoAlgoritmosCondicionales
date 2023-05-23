#8. Diseñar un algoritmo que muestre si una persona tiene ingresos o no, debe indicarlos ingresos y egresos, se debe validar el saldo , pero para ser más específicos se responderá a las siguientes preguntas:Elaborado por : Instructora Adriana Lucia Rincón ForeroSi no tiene efectivo entonces está en números rojos.Si tiene poco efectivo menor a 2000, que muestre que debe esforzarse portrabajar más.Si tiene un efectivo menor a 3000 entonces significa que le va regularmente bien.Si tiene un efectivo mayor a 3000 entonces significa que tiene buen status financiero

def status (quest1):
    
    if quest1 == "yes":
        
        income = float(input("Please enter the amount of income: "))
        expenditures = float(input("Put the number of outputs: "))
        total = income-expenditures
        
        if total < 2000:
            print("work harder")

        elif total in range (2001,2999):
            print("Half well")

        elif total >= 3000:
            print("you are very well financially")
            
    elif quest1 == "no":
        print("you are in a negative state")
        
    else:
        print("Error")
        
status(quest1=input("Do you have a good amount of income? yes or no?: "))