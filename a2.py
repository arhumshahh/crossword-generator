#ARHUM SHAH

blank = ' ' #makes 20 x 20 board out of spaces
board = [[ blank ] * 20 for i in range(20) ]

def printBoard(board): #prints the 20 x 20 board
  for i in range (len(board)):
    for j in range (len(board[i])):
      print(board[i][j], end = '')
    print()



def addFirstWord(board, word): #places first word on grid
  n=len(word)
  if n > 20: #if the length of the word is longer than the board print message and return false
     print("The Word", word , "Reaches Outside Grid") 
     return False
  else: #or else place word in the middle
    for k in range (n):
      board[9][(((20-n)//2) + k)] = word[k]





def addvertical(board, word) :#This function vertically adds a word to the crossword if there are no problems by placing them
  for i in range(len(board)) :#checks every space  in the board to see if a letter matches
    for j in range(len(board)) :
      if board[i][j] != " ":
        for k in range(len(word)):#checks every letter of the word to see if it matches
          wordletter = word[k]
          boardletter = board[i][j]
          if boardletter == wordletter: #if the letter on the board matches the letter in the word
            place= False #if this variable is true at after looping though everthing it means that the word can be placed without any problems 
            found = True #this variable tells the program that a matching letter was found and it now has to check if the word can be placed without any problems 
            if found == True:# if found is true the program checks if the word can be placed without any prob.
              for q in range(len(word)):#cycles through each letter in the word to see if there are any problems with placing
                if i-k+q > 19 or i-k+q<0: #if the letter in the word goes into negative false is returned
                  place = False
                  break
                if board[i-k+q][j] == word[q] or board[i-k+q][j] == " " : #if the letters beside match the words letter or are blank than place is true
                  place = True
                  if j-1 >=0: 
                    if board[i-k+q][j] == " " and  board[i-k+q][j-1] != " " :#checks to see if there are letters beside if so place is false
                      place = False
                      break
                  if j+1 <= 19:
                    if board[i-k+q][j] == " " and  board[i-k+q][j+1] != " "  :#checks to see if there are letters beside if so place is false
                      place = False
                      break
                  if i-k-1 >= 0:
                    if board[i-k-1][j] != " " or (i-k+q)<0 or (i-k+q)>19:#checks to see if there are letters at the end if so place is false
                      place = False
                      break
                    else: 
                      place = True
                  if i-k+len(word)<=19:
                    if board[i-k+(len(word))][j] != " "  or (i-k+q)<0 or (i-k+q)>19:#checks to see if there are letters at the end if so place is false
                      place = False
                      break
                    else: 
                      place = True
                else: 
                  place = False
                  break
              if place == True: #if place is true after checking through all possible instances it prints the word in that spot
                for t in range(len(word)):
                  board[i-k+t][j] = word[t]
                return True   
            else:
              return False 

def addhorizontal (board,word):#This function horizontally adds a word to the crossword if there are no problems by placing them
  for i in range(len(board)) :#checks every space  in the board to see if a letter matches
    for j in range(len(board)) :
      if board[i][j] != " ":
        for k in range(len(word)):#checks every letter of the word to see if it matches
          wordletter = word[k]
          boardletter = board[i][j]
          if boardletter == wordletter:#if the letter on the board matches the letter in the word
            place= False #if this variable is true at after looping though everthing it means that the word can be placed without any problems 
            found = True#this variable tells the program that a matching letter was found and it now has to check if the word can be placed without any problems 
            if found == True: # if found is true the program checks if the word can be placed without any prob.
              for q in range(len(word)):#cycles through each letter in the word to see if there are any problems with placing
                if j-k+q > 19 or j-k+q<0: #if the letter in the word goes into negative false is returned
                  place = False
                  break
                if board[i][j-k+q] == word[q] or board[i][j-k+q] == " " :#if the letters beside match the words letter or are blank than place is true
                  place = True
                  if i-1 >=0:
                    if board[i][j-k+q] == " " and  board[i-1][j-k+q] != " "  :#checks to see if there are letters beside if so place is false
                      place = False
                      break
                  if i+1 <= 19:
                    if board[i][j-k+q] == " " and  board[i+1][j-k+q] != " ":#checks to see if there are letters beside if so place is false
                      place = False
                      break
                  if j-k-1 >= 0 :
                    if board[i][j-k-1] != " " or (j-k+q)<0 or (j-k+q)>19:#checks to see if there are letters at the end if so place is false
                      place = False
                      break
                  if  j-k+len(word)<=19:#checks to see if there are letters at the end if so place is false
                    if board[i][j-k+(len(word))] != " "  or (j-k+q)<0 or (j-k+q)>19:
                      place = False
                      break
                    else: 
                      place = True
                else: 
                  place = False
                  break
              if place == True:#if place is true after checking through all possible instances it prints the word in that spot
                for t in range(len(word)):
                  board[i][j-k+t] = word[t]
                return True 
            else:
              return False


      
      
    

def crossword(L):
  firstWordAdded = False #checks if first words been added 
  counter = 0
  for i in L:
    i = i.lower()
    if firstWordAdded == False: #if first word isnt added and fits criteria it places it
      if addFirstWord(board, i) != False:
        firstWordAdded = True
        counter+=1
    elif counter %2 == 1 and firstWordAdded != False : #if its the an odd number it attemtps to place it vertially than horizontally if none work than prints message
      if addvertical(board, i) == True:
        addvertical(board, i)
        counter+=1
      elif addvertical(board, i) != True and addhorizontal(board, i) == True:
        addhorizontal(board, i)
        counter+=1
      elif addvertical(board, i) != True and addhorizontal(board, i) != True:
        print("the word:", i, "cannot be placed")
        counter+=1
    elif counter %2 == 0 and firstWordAdded != False:#if its the an even number it attemtps to place it horizonantally than vertically if none work than prints message
      if addhorizontal(board, i) == True:
        addhorizontal(board, i)
        counter+=1
      elif addhorizontal(board, i) != True and addvertical(board, i) == True:
        addvertical(board, i)
        counter+=1
      elif addvertical(board, i) != True and addhorizontal(board, i) != True:
        print("the word:", i, "cannot be placed")
        counter+=1
  printBoard(board) #prints the board 

  


  
#test case (this can be changed to any words)
crossword(["abcdefghijklmnopqrst",
               "fffffggg",
               "ttttttttttuuuuuuuuuz",
               "yzzz",
               "qqqqqqqqqqqqqqy",
               "xxxxxxxxxaaaaaaa",
               "aaaaggg",
               "xxwwww",
               "wwwwvvvvve",
               "vvvvvvvvvvvvq",
               "mat",
               "make",
               "maker",
               "remake","hat",])



