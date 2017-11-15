# This is my looping assignment by john paul lucia


ItemName = str()
CurrentPrice = float()


#Print welcome message
print("Welcome to Al's Auction")
print("This program will ask for the name of an item and the original price.")
print("It will then determine the discount of that item over 5 days.")
print()
#Outer loop stuff
# While loop
ItemCount = int(0)
#Name of your item
ItemName = "Antique Table"
#Price of item
CurrentPrice = 225.0

Discount = CurrentPrice * .1
for ItemCount in (1,2,3,4):


    ItemName = str()
    CurrentPrice = float()
    print()
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    ItemName = input("Enter the name of your item: ")
    CurrentPrice = float(input("Enter the original cost: "))
    print()
    print("Day\tDiscount\tDiscount Price\t")
    print("----------------------------------------------------------")
    

    # Inner loop stuff.....
    Discount = float()
    DiscountCount = int(0)
    while DiscountCount < 5:
        Discount = CurrentPrice * .1
        CurrentPrice = CurrentPrice - Discount
        DiscountCount += 1
        print(DiscountCount, "\t", "$", "%2.2f" % Discount, "\t\t" ,"$", "%2.2f" % CurrentPrice)