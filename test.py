def listChar(key):
    listChars=[]
    for char in key:
        if char not in listChars:
            listChars.append(char)
    return listChars

def palindrome(key):
    oddNumber = 0
    listchar= listChar(key)
    for char in listchar:
        if (key.count(char)%2 == 1):
            oddNumber += 1 
    if(oddNumber!=1):
        return(False)
    return(True)
            
key=""
while True:
    key=raw_input("type the anagram to lock the door : ")
    if len(key)< 10**5 and len(key)>=1:
        break
key=key.lower()
if (palindrome(key) == True):
    print "YES"
else:
    print "NO"






