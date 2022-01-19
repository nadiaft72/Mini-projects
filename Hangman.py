def findLetter (x , strWord):
    listOfPlaces = []
    a=0
    if strWord.find(x)== -1 :
        return -1
    else:
        start = strWord.find(x ,a)
        while start != -1 and start < len(strWord):
            listOfPlaces.append(start)
            a = start +1
            start = strWord.find(x ,a)

        return listOfPlaces



    return

#guess the word :)
strWord = "alphabet"
listStr = [" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]
count = 10
countOfCorrect = 0
print("you have 10 guess !") 
while count != 0 and countOfCorrect != len(strWord):
    
    x = input("enter a letter : ")
    res = findLetter(x,strWord)
    if res != -1 :
        if listStr[res[0]] == " _ " :
            countOfCorrect += len(res)
            for i in range(0,len(res)):
                listStr[res[i]] = x
            print("".join(listStr))
    else :
        count -= 1
        print("nope! you have ",count," guesses! :)")

if count == 0 :
    print("maybe later!")
else: 
    print("yayyyyy ! :)")