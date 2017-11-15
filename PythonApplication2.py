# This program is used to read 2 files. the first file is "Top25HalloweenSongs
#Contains halloween songs and the second one file is Top25HalloweenSongs_Comments
# contains a matching comment to the song information
# written on 10/16/17 by john paul lucia



HeaderStr = "## Welcome to my scary Halloween song selection program...Boo! ##"
print("#" * len(HeaderStr))
print(HeaderStr)
print("#" * len(HeaderStr))
print()

# Read in the song information file
Songs = list()
SongsFP = open("Top25HalloweenSongs.txt")
Songs = SongsFP.readlines()
SongsFP.close()


# Read in the song Comments file
SongComments = list()
SongsCommentsFP = open("Top25HalloweenSongs_Comments.txt")
SongComments = SongsCommentsFP.readlines()
SongsCommentsFP.close()


# Get the user's song selection.....
SongNumber = int(input("Please enter the song number:"))

#Test if user input is beyond number of lines in file...
while SongNumber >= len(Songs):
    print("Invalid input. Please try again...")
    SongNumber = int(input("Please enter the song number:"))

    # Split the song line into pieces parts....
SongLine = str()
SongLine = Songs[SongNumber - 1]

SongParts = list()
SongParts = SongLine.split(',')


# Print the Song Information.....
SongPrintStr = str()
SongPrintStr = "Song number " + SongParts[0] + " is from artist " + SongParts[1] + " and the song is " + SongParts[2]
print(SongPrintStr)

print()

print("----------\n")



#Split comment line into pieces parts 
SongCommentLine = str()
SongCommentLine = SongComments[SongNumber - 1]

SongCommentParts = list()
SongCommentParts = SongCommentLine.split('%')

#Print the song comments
print(SongCommentParts[1])

#Save the song selection to a file named "MyFavoriteHalloweenSong.txt"
SongSelectionFP = open("MyFavoriteHalloweenSong.txt", 'w')
SongSelectionFP.writelines(SongPrintStr) # Song Info
SongSelectionFP.writelines("\n")
SongSelectionFP.writelines(SongCommentParts[1]) # Song Comment
SongSelectionFP.close()





#print(Songs[SongNumber - 1], SongComments[SongNumber - 1])







EnderStr = "## Thank you...Boo! ##"
print("#" * len(EnderStr))
print(EnderStr)
print("#" * len(EnderStr))


