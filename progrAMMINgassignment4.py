# This is my programming assignment #4
# If it works John Paul wrote it. if it doesnt
# work idk who did

#Declare variables.....
itemName = str()
isFragile = str()
orderTotal = float()
destination = str()
shippingcost = float()


#Get input from user here.....
itemName = input("Please enter the item name:")
isFragile = input("Is the item fragile? (y=yes/n=no):")
orderTotal = float(input("Please enter your order total:"))
destination = input("Please enter destination. (usa/can):")

orderTotal = 50.00

# Now the branching........
if orderTotal < 50.00:
    # decide whether going to usa or can
    if destination == "usa":
        shippingcost = 6.00
    elif destination == "can":
        shippingcost = 8.00
    else:
        print("Invalid Destination")



elif orderTotal >= 50.00 and orderTotal <= 100.00:
    # decide whether going to usa or can
    if destination == "usa":
        shippingcost = 9.00
    elif destination == "can":
        shippingcost = 12.00
    else:
        print("Invalid Destination")

elif orderTotal > 100.00 and orderTotal <= 150.00:
    # decide whether going to usa or can
    if destination == "usa":
        shippingcost = 12.00
    elif destination == "can":
        shippingcost = 15.00
    else:
        print("Invalid Destination")

else:
    shippingcost = 0.00
    # decide whether going to usa or can

 

# add in if fragile...
if (isFragile == "y" or isFragile == "Y") and orderTotal < 150.00:
    shippingcost += 2.00

    # Pretty print here....... use '/t'
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Your item is :\t\t\t\t\t", itemName)
print("Your shipping cost is:\t\t\t\t $%0.2f" % shippingcost)
print("You are shipping to:\t\t\t\t", destination)
print("Your total shipping costs are:\t\t\t $%0.2f" % (orderTotal + shippingcost))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Thank you for your order")