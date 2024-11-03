'''Write a class train which has methods to book a ticket , get status (no of seats) and 
get fare information of trains running under indian railways.'''

class Train:

    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is : {self.name}")
        print(f"The seats available in the train are : {self.seats}")

    def getFareInfo(self):
        print(f"The price of the ticket is : {self.fare} Rs.")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked !! your seat number is: {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Train is full. kindly try in tatkal.")                

intercity = Train('Intercity Express : 120034',100,2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
