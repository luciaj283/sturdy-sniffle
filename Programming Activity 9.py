def intro():
    welcome = "********** Welcome to TicketsRUs **********"
    print(len(welcome) * '*')
    print(welcome)
    print(len(welcome) * '*')

class Ticket:
    def __init__(self,artist_name,event_date,venue_name,retail_price):
        self.__artist_name = artist_name
        self.__event_date = event_date
        self.__venue_name = venue_name
        self.__retail_price = retail_price
    
    def __str__(self):
        return ('\n\tThe Artist: %s \n\tThe Venue: %s \n\tThe price: %2.2f \n\tThe Date: %s' % (self.__artist_name, self.__venue_name, self.__retail_price, self.__event_date))

    def set_artist(self,artist_name):
        self.__artist_name = artist_name
    
    def get_artist(self):
        return self.__artist_name
    
    def set_eventdate(self,event_date):
        self.__event_date = event_date
    
    def get_eventdate(self):
        return self.__event_date
    
    def set_venue(self, venue_name):
        self.__venue = venue_name
    
    def get_venue(self):
         return self.__venue_name

    def set_price(self,retail_price):
        self.__retail_price

    def get_price(self):
        return self.__retail_price

def Main():
    numTickets = int(input("Please enter the number of tickets: "))
    ticketlist = list()
    while numTickets:

        artist_name = input("Please enter the artists name: ")
        event_date = input("Please enter the event date (e.g. 'Jun 1 2017 7PM'): ")
        venue_name = input("Please enter the venue name: ")
        retail_price = float(input("Please enter the ticket price: "))
        aTicket = Ticket(artist_name,event_date,venue_name,retail_price)
        
        ticketlist.append(aTicket)
        numTickets -= 1

    for aTicket in ticketlist:
        print(aTicket)

intro()
Main()
print('\n**********Thank you**********')