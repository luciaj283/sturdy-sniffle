# This is my programming assignment #3 - John Paul Lucia
score1 = 0
score2 = 0
score3 = 0
sumBoris = 0
avgBoris = 0.0
sumNatasha = 0.0
avgNatasha = 0.0
teamAvg = 0.0


# Print the *'s and introduction.....
print("************************************************************************")
print(" Welcome to the Bowling application for Boris and Natasha")
print("")
# Get input from user....


score1 = int(input("    Please enter Bori's score #1: "))
score2 = int(input("    Please enter Bori's score #2: "))
score3 = int(input("    Please enter Bori's score #3: "))

sumBoris = score1 + score2 + score3
avgBoris = sumBoris / 3


print("")
score1 = int(input("    Please enter Natasha's score #1: "))
score2 = int(input("    Please enter Natasha's score #2: "))
score3 = int(input("    Please enter Natasha's score #3: "))

sumNatasha = score1 + score2 + score3
avgNatasha = sumNatasha / 3

print("")
print("...And now the averages...")

teamAvg = (avgBoris + avgNatasha) / 2

print('          Boris'' average is %2.2f' % avgBoris)
print('          Natashas'' average is %2.2f' % avgNatasha)
print('          The teams'' average is %2.2f' % teamAvg)
print("*****************************************************************")
print("Thank you")