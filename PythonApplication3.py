print('**************************************************')
print('Welcome to my Substitution Cipher Program ********')
print('**************************************************')
print()


PlainTextStrings = str()
PlainTextStringsFT = open("original.txt")
PlainTextStrings = PlainTextStringsFT.readlines()
PlainTextStringsFT.close
cipherstringslist = list()

for aString in PlainTextStrings:
    cipherStr = str()           #For each string in the plain text file
    aString = aString.strip()
    for c in aString: # for each character in the string from the file..
        intChar = ord(c)
        if intChar >= 48 and intChar <= 57:
            break
        elif c == 'a' or c == 'A':
            cipherStr += '1'
        elif c == 'e' or c == 'E':
            cipherStr += '2'
        elif c == 'i' or c == 'I':
            cipherStr += '3'
        elif c == 'o' or c == 'O':
            cipherStr += '4'
        elif c == 'u' or c == 'U':
            cipherStr += '5'
        elif c == 'y' or c == 'Y':
            cipherStr += '6'
        elif c == ' ':
            cipherStr += '7'
        else:
            cipherStr += c

    print(aString)
    print(cipherStr + '\n')
    
    cipherstringslist.append(cipherStr + '\n')
       





FP = open("cypher.txt", 'w')
FP.writelines(cipherstringslist)
FP.flush()
FP.close()


#print(PlainTextStrings[0], cipherstringslist[0])
#print(PlainTextStrings[1], cipherstringslist[1])
#print(PlainTextStrings[2], cipherstringslist[2])
#print(PlainTextStrings[3], cipherstringslist[3])
#print(PlainTextStrings[4], cipherstringslist[4])
#print(PlainTextStrings[5], cipherstringslist[5])
#print(PlainTextStrings[6], cipherstringslist[6])
#print(PlainTextStrings[7], cipherstringslist[7])
#print(PlainTextStrings[8], cipherstringslist[8])
#print(PlainTextStrings[9], cipherstringslist[9])

print()
print("********** Thank you**********")
print("******************************")




#for o in line:
   # if o == '4'
  #  cipherStr += '4'







 # ample_str = "We hold these Truths to be self evident that all Men are created equal."
#aString = list()
#cipherstringslist = list()



    # elif c == 'e' or c == 'E':
        #    cipherStr += '2'
            #the rest of the vowels and y and space 
#else:
     # cipherStr += c
    #  cipherstringslist.append(cipherStr)
            

