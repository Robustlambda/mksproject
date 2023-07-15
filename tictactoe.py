import random
board =["-","-","-",
        "-","-","-",
        "-","-","-"]
currentplayer = "x"
winner = None
gamerunning = True

def printingboard(board):
    print(board[0] +"\t""|" "\t"+ board[1] +"\t""|" "\t"+ board[2])
    print("-----------------")
    print(board[3] +"\t""|" "\t"+ board[4] +"\t""|" "\t"+ board[5])
    print("-----------------")
    print(board[6] +"\t""|" "\t"+ board[7] +"\t""|" "\t"+ board[8])
printingboard(board)

def playerinput(board):
    inp = int(input("Enter the place to set your symbol:"))
    if inp>=1 and inp<=9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops! already a player in that place")
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] == board[1] !="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] == board[3] !="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] == board[6] != "-":
        winner = board[6]
        return True

def checkrows(board):
    global winner
    if board[0] == board[3]== board[6] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] !="-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] !="":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8]== board[0] !="-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] == board[2] !="-":
        winner = board[2]
        return True

def checktie(board):
    global gamerunning
    if "-" not in board:
        printingboard(board)
        print("Its a tie!")
        gamerunning = False

def checkwin():
    if checkdiagonal(board) or checkrows(board) or checkhorizontal(board):
        print(f"The winner is {winner}")

def switchplayer():
    global currentplayer
    if currentplayer == "x":
        currentplayer ="o"
    else:
        currentplayer = "x"

def computer(board):
    while currentplayer == "o":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] ="o"
            switchplayer()




while gamerunning:
    printingboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()


