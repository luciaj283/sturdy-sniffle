# This is a shell of the program to help you get started..
import turtle
image = "bee.gif"

# Create the Turtle objects
scrnObj = turtle.Screen()
drwObj = turtle.Turtle()

def PrintHeader(name):
    print('*' * 50)
    print('*' * 10, "Welcome to my Turtle Program", '*' * 10)
    print('*' * 50)

    # Pretty print the introduction to the program...
    #.....To Do

def GetColors():
    lineColor = input("Please enter the line color your choices are 'black', 'red ,'blue':")
    bkColor = input("Please enter the background color. Your choices are 'white','pink','gold','blue':")
    print()
    
    # Prompt the user for the line color and the background color
    #.....To Do
    return lineColor, bkColor

def GetCoordinates():
    coords = list()
    # Open file and read in the bee paths....
    fp = open("BeePaths.txt")
    coords = fp.readlines()
    fp.close()

    #.....To Do
    return coords

def InitTurtle(screenname = 'Turtle', lineClr = 'blue', bkClr = 'gold'):
    # Set screen object...
    global scrnObj
    scrnObj.setup(500, 500)
    scrnObj.title(screenname)
    scrnObj.addshape(image)
    scrnObj.bgcolor(bkClr)

    # Set turtle object...
    global drwObj
    drwObj.hideturtle()
    drwObj.speed(1)
    drwObj.color(lineClr)
    drwObj.shape(image)
    

def Draw():
    coords = GetCoordinates()
    #coords = ['72,-105\n','158,56\n','13,11\n']
    for coord in coords:
        print(coord)
        coordlist = coord.split(',')
        x = coordlist[0]
        y = coordlist[1].strip()
        


    # Convert "coord" into an X and Y coord...
    # Draw line and "stamp" bee.
        global drwObj
        drwObj.goto(int(x),int(y))
        drwObj.stamp()


def main():
    Title = "Turtle"
    PrintHeader(Title)
    
    lineColor, bkColor = GetColors()

    InitTurtle()
    
    scrnObj.listen()
    Draw()
    scrnObj.exitonclick()


main()