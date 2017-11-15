import datetime

# Create a new date object representing the current date (May 30, 2016)
today  = datetime.date.today()
jersey_number = 123
number_of_hits = 5
number_of_times_at_bat = 6
batting_average = (number_of_hits)/(number_of_times_at_bat)


print('**************', today.strftime('%B %d %Y'),'************')
print('Welcome to my Batting statistics program')
print('*****************************************')

name_of_the_player = input("Please enter the name of the Player:")
jersey_number = input("Please enter the name of the player's jersey number:")
number_of_hits = input("Please enter the name of the player's number of hits:")
number_of_times_at_bat = input("Please enter the player's number of times at bat:")



print(name_of_the_player, "whose jersey number is", jersey_number, "had a batting average of %2.4f." % batting_average,)
