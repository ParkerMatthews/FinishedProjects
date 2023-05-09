with open("Book1.csv","r") as file1:
    masterlist=[]
    for line in file1.readlines():
        currentlist=line.strip().split(",")
        masterlist.append(currentlist)
def search(uiword,letters):
    lettertosearchfor=uiword[0]
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            if lettertosearchfor == letters[i][j]:
                x=onehoriz_search(i,j,uiword)
                if x is not None: #is checks type of varible loves the word None
                    print(f"{uiword} is at ({i},{j}")
                elif twohoriz_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif onevert_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif twovert_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif brdiagon_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif tldiagon_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif bldiagon_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                elif trdiagon_search(i, j, uiword) is not None:
                    print(f"{uiword} is at ({i},{j}")
                 
def onehoriz_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if j+k < len(masterlist[i]):
                if hword[k] == masterlist[i][j+k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def twohoriz_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (j-k) >= 0:
                if hword[k] == masterlist[i][j-k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def onevert_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i-k) >= 0:
                if hword[k] == masterlist[i-k][j]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def twovert_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i+k) < (len(masterlist)):
                if hword[k] == masterlist[i+k][j]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def brdiagon_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i+k) < (len(masterlist)) and j+k < len(masterlist[i]):
                if hword[k] == masterlist[i+k][j+k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def bldiagon_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i+k) < (len(masterlist)) and (j-k) >= 0:
                if hword[k] == masterlist[i+k][j-k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def trdiagon_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i-k) >= 0 and j+k < len(masterlist[i]):
                if hword[k] == masterlist[i-k][j+k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
def tldiagon_search(i,j,hword):
    # i = row , j = collium
        flag = True
        for k in range(len(hword)):
            if (i-k) >= 0 and j-k >= 0:
                if hword[k] == masterlist[i-k][j-k]:#to change direction j-k
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            print("Found the word!")
            return i , j
    #TODO:use a loop to match the rest of the word
    #Look to the right of the first found letter.
    #Looking for the letter too the right of the found letter.
    #After found 2nd letter repeat.
    #After word is found let the program keep running. 
    
    #Search from left to right to check for the word
    #Repeat unitl reach end of puzzle
    #a,b,c,c,a,t,a,b,c
               
search("BINARY",masterlist)
search("COMPUTERSCIENCE",masterlist)
search("DECIMAL",masterlist)
search("HEXADECMIAL",masterlist)
search("JUPYTER",masterlist)
search("MATPLOTLIB",masterlist)
search("NOTEBOOK",masterlist)
search("OCATAL",masterlist)
search("PANDAS",masterlist)
search("POWERSHELL",masterlist)