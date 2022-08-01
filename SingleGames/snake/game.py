import numpy as np
import random
RUN = True
def removeLast(board,x,y,len):
    for i in range(len):
        
        if board[y][x]
    return board

def updateSnake(board,x,y,len):
    if board[y][x] == 0:
        removeLast(board,x,y,len)
    if board[y][x] == 3:
        endGame()
    return board, x, y, len
def endGame():
    RUN = False
    print("game over")
def updateBoard(board,x,y,len):
    return board, x, y, len

def moveSnake(x,y,dir):
    if dir =="N":
        y += 1
    if dir =="E":
        x += 1
    if dir =="S":
        y -= 1
    if dir =="W":
        x -= 1
    return x,y

def generateFood(board):
    run = True
    while run:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if board[y][x] == 0:
            board[y][x] = 1
            run = False
    return board
def printBoard(len, x, y, dir, board):
    print(board)

def main():
    
    # each spot on board has different states
    # Board Unit States:
    # 0 : Empty
    # 1 : Food
    # 2 : Snake Head
    # 3 : Snake Body
    snakeLen = 3
    snakeXPos = 4
    snakeYPos = 4
    snakeDir = "N"

    board = np.zeros((10,10))
    for i in range(snakeLen):
        if i == 0:
            board[snakeYPos][snakeXPos] = 2
        else:
            board[snakeYPos][snakeXPos-i] = 3
    board = generateFood(board)

    # Game Loop 
    while RUN:
        snakeXPos,snakeYPos = moveSnake(snakeXPos, snakeYPos)
        board, snakeXPos, snakeYPos, snakeLen = updateSnake(board, snakeXPos, snakeYPos, snakeLen)
        board, snakeXPos, snakeYPos, snakeLen = updateBoard(board, snakeXPos, snakeYPos, snakeLen)



main()