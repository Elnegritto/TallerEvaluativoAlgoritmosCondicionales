#25. Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:a. ¿Puede volar?b. ¿Es humano?c. ¿Tiene máscara?


ListSuperheroes = ["Iron Man","La Bruja Escarlata","Thor","Hulk","Pantera Negra"]

def guess (quest1, quest2, quest3):

    if quest1 == "yes":
        
        if quest2 == "yes":
                
            if quest3 == "no":
                print(f"Your characters can be: {ListSuperheroes[1]}")
            
        elif quest2 == "no":
                
            if quest3 == "no":
                print(f"Your characters can be: {ListSuperheroes[0,2]}")
            
    elif quest1 == "no":
        
        if quest2 == "yes":
            
            if quest3 == "yes":
                print(f"Your characters can be: {ListSuperheroes[4]}")
                
            elif quest3 == "no":
                print(f"Your characters can be: {ListSuperheroes[3]}")
        
    else:
        print("This superhero is not on the list at the moment")
    
print("This superhero is not on the list at the moment")
guess(quest1=input("Can it fly ?: "), quest2=input("It is human?: "), quest3=input("Does it have a mask?: "))

