#Programmer: Timothy Pickering
#Date: 2/13/25
#Title: Movie Tix 2.0

# Dear instructor, I created a working program based on assignment requirements, but it felt unfinished since the program asks what movie(s) but only prints the ticket total.
# I wanted to be able to print the number of tickets next to the movie title as to me this seemed closer to a real world application, at least logic-wise.
# Lines 10, 17-20, 23-24 are what was added above and beyond the assignment scope, so sorry if this hard to grade but some extra credit would be dope!

ticketsTotal = 0 #accumulator initialization
moviesList = {} #to store movie names and ticket counts
while True:
    response = input("Would you like to see a movie?(yes/no): ").lower()
    if response == "yes": #run if response is yes
        movieName = input("Enter the movie name: ")
        ticketCount = int(input(f"How many people are watching {movieName}?: ")) #number to add to ticketsTotal
        ticketsTotal = ticketsTotal + ticketCount #running total
        if movieName in moviesList:
            moviesList[movieName] = moviesList[movieName] + ticketCount #add to existing movie
        else:
            moviesList[movieName] = ticketCount #create a new entry
    else: #run if response is no
        print(f"Here are your ticket(s): {ticketsTotal}") #assignment directive
        for movie, count in moviesList.items(): #prints ticket groups
            print(f"-{movie}: {count} ticket(s)")
        print("Enjoy your night!")
        break   #Exit the loop
