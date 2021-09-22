"""1.	Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
Decide how many number of buses required"""
no_of_people=int(input("total no.of people:"))
no_of_seats=int(input("no.of seats:"))
no_of_buses=no_of_people//no_of_seats
print(no_of_buses)
