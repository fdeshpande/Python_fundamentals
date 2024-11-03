class railwayreserve:
    print("WELCOME TO THE RAILWAY RESERVATION PLATFORM !!!")
    print("WE WILL BE HAPPY TO SERVE YOU !!!!")
    name =input("Enter your name:\t")
    gender = input("Enter your gender:\t")
    quota = input("Enter your preference whether its general/ ladies /sleeper /AC 1stclass /AC 2nd / AC 3rd class:\t")
    seat = input("Enter your seat preference whether it is window-side / no preference:\t")
    print(''' ***************** TRAIN AVAILABLITY DETAILS *******************
        
               searching........
               
               Maharashtra Exp--990342 ___at 4:00 pm__starts from Nagpur__to__Pune____departure at 4:02pm...\n
               Itwari_Dongargarh_Local--002343___at 3:30 pm__starts from Itwari__to__Dongargarh at 3:45pm...\n
               Vidarbha Exp--028843___at 8:30 am__starts from Nagpur__to__Mumbai____departure at 3:45pm...\n
                
                here are some information of train .......
                As per your preference you can reserve your seat....asap.
                Thank you!!!!
                ''')
    traininfo = input("Enter your train name /number:\t")

    def passengerinfo(self):
        print(f"Name : \t{self.name}")  
        print(f"Gender : \t{self.gender}")
        print(f"Seat Preference : \t{self.seat}")
        print(f"Quota Preference : \t{self.quota}")
    
    def train_info(self):
                
        print(f"Your train booking Status is for :\t{self.traininfo} rail.")   
        print("THANK YOU !!!!!ENJOY YOUR JOURNEY!!!!!")  

reservation = railwayreserve()
reservation.passengerinfo()
reservation.train_info()
