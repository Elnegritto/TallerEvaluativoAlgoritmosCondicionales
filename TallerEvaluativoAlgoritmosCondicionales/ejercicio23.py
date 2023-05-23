#23. Un cliente va a comprar una moto y se percata que si lo compraba el día martes tiene un descuento del 10%, luego si lo compra el día sábado tiene un descuento del 18% mostrar cuanto pagara en cada opción.

valueMotorcycle = int(input("Write the value of the motorcycle: "))
disccountTuesday = valueMotorcycle * 0.1
totalTuesday = valueMotorcycle - disccountTuesday
disccountSaturday = valueMotorcycle * 0.18
totalSaturday = valueMotorcycle - disccountSaturday

def pay (day):
    
    if day == "tuesday" or day == "TUESDAY":
        print(f"The cost of the motorcycle on Tuesday is: {totalTuesday}")
        
    elif day == "saturday" or day == "SATURDAY":
        print(f"The cost of the motorcycle on Saturday is: {totalSaturday}")
    
    else:
        print("Discounts are not available or applicable for this day")
        
pay(day=input("Insert day: "))