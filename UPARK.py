#define the function
def UPARK():
        pass

        #state what the program does
        print("\nThis program tells JMU students what equipment they are renting at UPARK.\n")

        print("Yes = 1")
        print("No = 2")

        start = int(input("\nHow many credits do you have? Yes or No :"))
        if start >= 7 :
                print("\nChoose one of the equipment options below.\n")
        elif start < 7 : 
                print("\nInsufficient Credits.")
                quit("\nUPARK")
                               
        equipment = ["Soccerball = 1, Basketball = 2, Football = 3, Tennis Racquets = 4, Volleyball = 5, Kayak = 6, Tennis Balls = 7"]                    
        print(*equipment, sep='\n')
         

        #define what equipment you want to rent out
        int(input("Please enter the equipment you wish to rent: "))                if input = 1:
                        print("\nYou have rented the Soccerball.")
                elif input == 2:
                        print("\nYou have rented the Basketball.")
                elif input == 3:
                        print("\nYou have rented the Football.")
                elif input == 4:
                        print("\nYou have rented the Tennis Racquets.")
                elif input == 5:
                        print("\nYou have rented the Volleyball.")
                elif input == 6:
                        print("\nYou have rented the Kayak.")
                elif input == 7:
                        print("\nYou have rented the Tennis Balls.")

                        print("\nPlease look at the options below.\n")

                #define how long you want to rent the equipment out for
                renttime = int(input("Please enter the time for how long you want to rent the equipment out for. :"))
                if renttime = 8 
                        print("\nYou have rented your equipment for 1 hour. Thank you for using this program.\n")
                        if renttime > 17 and renttime <= 31:
                                quit("UREC")
                elif renttime > 31:
                        print("You may not go to rent at this time, please choose another time.\n")
                elif renttime < 17:
                        print("You may not go to rent at this time, please choose another time.\n")

        print("1 hour = 8")
        print("2 hours = 9")       
        print("3 hours = 10")
        print("4 hours = 11")
        print("5 hours = 12")
        print("1 day = 13")
        print("2 days = 14")
        print("3 days = 15")
        

        #define what time you want to rent your equipment
        renttime = int(input("Please enter the time at which you would like to rent your equipment:"))
        if renttime > 14 and renttime <= 31:
                print("\nYou may rent. Thank you for using this program.\n") 
                quit("\nUREC")
        elif renttime > 31:
                print("You may not go to the gym.\n")
        elif renttime < 14:
                print("You may not go to the gym.\n")
                
UPARK()
