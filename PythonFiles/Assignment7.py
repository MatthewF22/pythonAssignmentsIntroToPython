# Print cost of speeding ticket based on how high over the limit you are
# The rate changes in increments based on 1-5mph over, 6-10mph over, and so on
#I got ticket prices from this website and based it loosly off their math https://www.dwicriminallawcenter.com/missouri-speeding-ticket-cost/#:~:text=1-5%20mph%20over%20the,over%20the%20speed%20limit%3A%20%24149
# Matthew Franklin, October 2022

def get_ticket_price(speed_limit, your_speed):
    #This collects the speed_limit and your_speed from the user
    #It then calculates the total ticket cost based on how high above the speed limit they are
    #See comments on each statement for specific calculations

    minimum_cost = 85.0
    if your_speed >= speed_limit + 26:
        #for speed 26mph + over the speed limit
        return("jail time for reckless driving")
    elif your_speed >= speed_limit + 20:
        #for speed 20 - 25mph over the limit
        return (minimum_cost * 1.6) + minimum_cost
    elif your_speed > speed_limit + 15:
        #for speed 16 - 19mph over the limit
        return (minimum_cost * 0.76) + minimum_cost
    elif your_speed > speed_limit + 10:
        #for speed 11 - 15mph over the limit
        return (minimum_cost * 0.45) + minimum_cost
    elif your_speed > speed_limit + 5:
        #for speed 6 - 10mph over the limit
        return (minimum_cost * 0.18) + minimum_cost
    elif your_speed >= speed_limit + 1:
        #for speed 1 - 5mph over the limit
        #minimum cost of ticket is 85.0
        return minimum_cost
    else:
        #for if the user doesn't deserve a speeding ticket
        return "nothing, you weren't speeding"

def isValidInput(speed_limit, your_speed):
    """ returns True if speed_limit and your_speed are greater than 0, False otherwise """
    """ Both need to be above 0 because you can't have a road with 0 speed limit or a car traveling at 0 mph"""
    return speed_limit > 0 and your_speed > 0

def main ():
    #Assigned_speed_limit is the actual speed limit on the road
    #actual_speed is the speed that the user was driving at
    assigned_speed_limit = int(input("What was the speed limit of the road: "))
    actual_speed = int(input("What speed were you driving at: "))
    #while loops makes the user reenter the values if one is not acceptable
    while not isValidInput(assigned_speed_limit, actual_speed):
        assigned_speed_limit = int(input("What was the speed limit of the road: "))
        actual_speed = int(input("What speed were you driving at: "))
    #ticket_cost calls the function get_ticket_price to find the ticket cost using the perameters inputed by the user
    ticket_cost = get_ticket_price(assigned_speed_limit, actual_speed)
    print("Your ticket will cost,", ticket_cost, "!")

    #Below is the original code prior to the use of the while loop
    """if isValidInput(assigned_speed_limit, actual_speed):
        ticket_cost = get_ticket_price(assigned_speed_limit, actual_speed)
        print("Your ticket will cost,",ticket_cost,"for going",speed_difference,"over the limit!")
    else:
        print(assigned_speed_limit, "or", actual_speed , "is not a valid input:")"""

main()
