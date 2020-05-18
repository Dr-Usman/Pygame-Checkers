
import pygame
from pygame.locals import *

pygame.init()

wlcscr= pygame.display.set_mode((700,500))
strimg= pygame.image.load("image.jpg").convert_alpha()
    # Change resolution
window = pygame.display.set_mode((820, 660))
    # Set Title
pygame.display.set_caption("Checkers Game by Usman & Bava")


#colors
black = (0, 0, 0)
liteblack = (25, 25, 25)
white = (255, 255, 255)
litegrey = (230, 230, 230)
bgColor = (255, 206, 158)   #light brown
boundaryColor = (154, 83, 5) #Dark brown
cboxColor = (209, 139, 71)  #checkbox

#Create 2D array
# 0=Black, 1= white, -1=empty, none=invalid move
arr2d = [[None,0,None,0,None,0,None,0],
         [0,None,0,None,0,None,0,None],
         [None,0,None,0,None,0,None,0],
         [-1,None,-1,None,-1,None,-1,None],
         [None,-1,None,-1,None,-1,None,-1],
         [1,None,1,None,1,None,1,None],
         [None,1,None,1,None,1,None,1],
         [1, None, 1,None, 1,None, 1,None]
         ]

blackCount=0
whiteCount=0
for r in range(8):
    for c in range(8):
        if(arr2d[r][c]==0):
            blackCount+=1
        elif arr2d[r][c]==1:
            whiteCount+=1

print(blackCount,whiteCount)

def main():

    wlcscr.fill(bgColor)
    wlcscr.blit(strimg,(10,20))
    pygame.display.update()
    for i in range(10):
        pygame.time.delay(100)

    # change Background color
    window.fill(bgColor)
    # call boundary to make a line
    makeBoundaryline()
    # Make checkBoxes
    drawCheckboxes()
    # Place Pieces on board
    placePieces()
    player_Turn = 1
    print("Player {} Turn".format(player_Turn))

    gameLoop = True
    while gameLoop:

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                #print(x, y)
                mx, my = getPosition(x, y)
                #print("square", mx, my)

                if isPiece(mx, my):

                    if isBlackPiece(mx, my) and player_Turn==1:  # Black piece Movement
                        print("BLack")
                        if pygame.mouse.get_pressed()[0]:       #left key
                            print("left click")
                            if mx > 1 and my<8: # left & botttom
                                # next is not black and next to next is empty
                                if (not(arr2d[my][mx-2]==0 )) and arr2d[my+1][mx-3]==-1:

                                    if mx < 9and my<7:

                                        if arr2d[my][mx-2]==1 :
                                            print("Kill")
                                            killWhitepieceAtLeft(mx,my)
                                            player_Turn=2

                                            print("Player {} Turn".format(player_Turn))
                                            continue
                                    else:
                                        print("indexOutofBound")

                                if (not(arr2d[my][mx-2]==1)) and arr2d[my][mx-2]==-1:
                                    moveBlackPieceLeft(mx, my)
                                    player_Turn = 2
                                    print("Player {} Turn".format(player_Turn))

                                else:
                                    print("Piece L!")
                            else:
                                print("Bound!")

                        elif pygame.mouse.get_pressed()[2]:       #right key
                            if mx<8 and my <8 :       #right & bottom
                                #next not black
                                if (not(arr2d[my][mx]==0)) :
                                    if mx<7 and my<7:
                                        #next is white and next to next is empty
                                        if arr2d[my][mx]==1 and arr2d[my+1][mx+1]==-1:
                                            print("kill")
                                            killWhitepieceAtRight(mx, my)
                                            player_Turn = 2
                                            print("Player {} Turn".format(player_Turn))
                                            continue
                                    else:
                                        print("indexOutofBound")

                                if (not(arr2d[my][mx]==1)) and arr2d[my][mx]==-1:
                                    moveBlackPieceRight(mx, my)
                                    player_Turn =2
                                    print("Player {} Turn".format(player_Turn))

                                else:
                                    print("Piece R!!")
                            else:
                                print("Bound!")
                    '''else:
                        print("Click on Black!")'''


                    if isWhitePiece(mx,my) and player_Turn==2:       #white piece Movement
                        print("White")
                        if pygame.mouse.get_pressed()[0]:  # left key
                            print("left click")
                            if mx > 1 and my>1:
                                if not (arr2d[my-2][mx-2] == 1):
                                    if arr2d[my-2][mx-2]==0 and arr2d[my-3][mx-3]==-1:
                                        print("Goo")
                                        killBlackpieceAtLeft(mx,my)
                                        player_Turn = 1
                                        print("Player {} Turn".format(player_Turn))
                                        continue

                                if (not(arr2d[my - 2][mx - 2] == 0)) and arr2d[my - 2][mx - 2] == -1:
                                    moveWhitePieceLeft(mx, my)
                                    player_Turn=1
                                    print("Player {} Turn".format(player_Turn))
                                else:
                                    print("Piece L!")
                            else:
                                print("Bound!")

                        elif pygame.mouse.get_pressed()[2]:  # right key
                            if mx<8 and my>1:
                                if not (arr2d[my-2][mx] == 1):
                                    if mx<7 and my>0:
                                        if arr2d[my-2][mx]==0 and arr2d[my-3][mx+1]==-1:
                                            killBlackpieceAtRight(mx,my)
                                            player_Turn = 1
                                            print("Player {} Turn".format(player_Turn))
                                            continue
                                    else:
                                        print("indexOutofBound")

                                if not(arr2d[my - 2][mx] == 0) and arr2d[my - 2][mx] == -1:
                                    moveWhitePieceRight(mx, my)
                                    player_Turn=1
                                    print("Player {} Turn".format(player_Turn))
                                else:
                                    print("Piece R!!")
                            else:
                                print("Bound!")
                    else:
                        print("Invallid Move or Player {} Turn".format(player_Turn))


                else:
                    print("Click on Piece!")


        pygame.display.update()
    pygame.quit()



def getPosition(x,y):
    mx = int((x / 100) + 1)
    my = int((y / 80) + 1)
    return mx, my

def moveBlackPieceRight(x,y):
    mx,my = x,y
    # draw circle on next right pos
    pygame.draw.circle(window, black, [(((mx) * 100) + 60), (((my) * 80) + 50)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #next right pos=black
    arr2d[my][mx] = 0
    print("Black piece moved Right")

def moveBlackPieceLeft(x,y):
    mx,my = x,y
    # draw circle on next left pos
    pygame.draw.circle(window, black, [(((mx-1) * 100) - 40), ((my * 80) + 50)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #next pos=black
    arr2d[my][mx-2] = 0
    print("Black piece moved left")

def moveWhitePieceLeft(x,y):
    mx,my = x,y
    # draw circle on next left pos
    pygame.draw.circle(window, white, [(((mx-1) * 100) -40), (((my-1) * 80) - 30)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #next pos=white
    arr2d[my-2][mx-2] = 1
    print("White piece moved left")

def moveWhitePieceRight(x,y):
    mx,my = x,y
    # draw circle on next right pos
    pygame.draw.circle(window, white, [(((mx) * 100) +60), (((my-1) * 80) - 30)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #next pos=white
    arr2d[my-2][mx] = 1
    print("White piece moved right")

def killWhitepieceAtRight(x,y):
    mx, my = x, y
    # draw circle on next from next right pos
    pygame.draw.circle(window, black, [(((mx+1) * 100) + 60), (((my+1) * 80) + 50)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    #draw square on op piece
    pygame.draw.rect(window, cboxColor, (((mx * 100) + 10), ((my * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #op pos= empty
    arr2d[my][mx] = -1
    # next to next right pos=black
    arr2d[my+1][mx+1] = 0
    print("white piece killed at Right")

def killWhitepieceAtLeft(x,y):
    mx, my = x, y
    # draw circle on next from next left pos
    pygame.draw.circle(window, black, [(((mx-2) * 100) -40), (((my+2) * 80) - 30)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    #draw square on op piece
    pygame.draw.rect(window, cboxColor, ((((mx-2) * 100) + 10), (((my) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    #op pos= empty
    arr2d[my][mx-2] = -1
    # next to next left pos=black
    arr2d[my+1][mx-3] = 0
    print("white piece killed at Left")

def killBlackpieceAtLeft(x,y):
    mx, my = x, y
    # draw circle on next to next left pos
    pygame.draw.circle(window, white, [(((mx - 2) * 100) - 40), (((my - 2) * 80) - 30)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    #draw square on op piece
    pygame.draw.rect(window, cboxColor, ((((mx - 2) * 100) + 10), (((my - 2) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    # op pos = empty
    arr2d[my-2][mx-2] = -1
    # next pos=white
    arr2d[my - 3][mx - 3] = 1
    print("Black piece Killed at left")

def killBlackpieceAtRight(x,y):
    mx, my = x, y
    # draw circle on next to next right pos
    pygame.draw.circle(window, white, [(((mx + 2) * 100) - 40), (((my -2) * 80) - 30)], 40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor, ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    #draw square on op piece
    pygame.draw.rect(window, cboxColor, ((((mx ) * 100) + 10), (((my - 2) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    # op pos = empty
    arr2d[my-2][mx] = -1
    # next pos=white
    arr2d[my - 3][mx +1] = 1
    print("Black piece Killed at right")


def moveBKright(mx,my):
    pygame.draw.circle(window, black, [(((mx) * 100) + 60), (((my - 1) * 80) - 30)],
                       40)
    # draw sqaure on current pos
    pygame.draw.rect(window, cboxColor,
                     ((((mx - 1) * 100) + 10), (((my - 1) * 80) + 10), 100, 80))
    # current pos = empty
    arr2d[my - 1][mx - 1] = -1
    # next pos=black
    arr2d[my - 2][mx] = 0

def checkPieceExist(mx,my):
                # black k agy B/W,          white k agy b/w
        return not ((arr2d[my][mx] == 1) or (arr2d[my][mx] == 0))# and arr2d[my][mx-2]==-1
        #return arr2d[my][mx]==-1 or arr2d[my][mx-2]==-1

def isKing(x,y):
    if isPiece(x,y) and x>0 and x<9:
        if arr2d[y-1][x-1]==0and y==8:
            return 00
        if arr2d[y-1][x-1]==1and y==1:
            return 11

def isPiece(mx,my):
    #is clicked on black or white piece
    return (arr2d[my - 1][mx - 1] == 1) or (arr2d[my - 1][mx - 1] == 0)

def checkBound(mx,my):
    return (mx < 8) and  (mx > 1)

def isBlackPiece(mx,my):
    return arr2d[my - 1][mx - 1] == 0

def isWhitePiece(mx,my):
    return arr2d[my - 1][mx - 1] == 1

def isBlackKing(mx,my):
    if my==8:
        return True
    else:
        return False


def makeBoundaryline ():
    # Draw boundary line
    x = 0
    y = 0
    width = 10
    height = 650

    # boundary line
    pygame.draw.rect(window, boundaryColor, (x, y, width, height))  # left
    pygame.draw.rect(window, boundaryColor, (810, 0, width, height))  # right
    pygame.draw.rect(window, boundaryColor, (x, y, 810, 10))  # top
    pygame.draw.rect(window, boundaryColor, (x, 650, 820, 10))  # bottom

def drawCheckboxes():
    # Line1
    pygame.draw.rect(window, cboxColor, (110, 10, 100, 80))
    pygame.draw.rect(window, cboxColor, (310, 10, 100, 80))
    pygame.draw.rect(window, cboxColor, (510, 10, 100, 80))
    pygame.draw.rect(window, cboxColor, (710, 10, 100, 80))
    # line2
    pygame.draw.rect(window, cboxColor, (10, 90, 100, 80))
    pygame.draw.rect(window, cboxColor, (210, 90, 100, 80))
    pygame.draw.rect(window, cboxColor, (410, 90, 100, 80))
    pygame.draw.rect(window, cboxColor, (610, 90, 100, 80))
    # Line3
    pygame.draw.rect(window, cboxColor, (110, 170, 100, 80))
    pygame.draw.rect(window, cboxColor, (310, 170, 100, 80))
    pygame.draw.rect(window, cboxColor, (510, 170, 100, 80))
    pygame.draw.rect(window, cboxColor, (710, 170, 100, 80))
    # line4
    pygame.draw.rect(window, cboxColor, (10, 250, 100, 80))
    pygame.draw.rect(window, cboxColor, (210, 250, 100, 80))
    pygame.draw.rect(window, cboxColor, (410, 250, 100, 80))
    pygame.draw.rect(window, cboxColor, (610, 250, 100, 80))
    # Line5
    pygame.draw.rect(window, cboxColor, (110, 330, 100, 80))
    pygame.draw.rect(window, cboxColor, (310, 330, 100, 80))
    pygame.draw.rect(window, cboxColor, (510, 330, 100, 80))
    pygame.draw.rect(window, cboxColor, (710, 330, 100, 80))
    # line6
    pygame.draw.rect(window, cboxColor, (10, 410, 100, 80))
    pygame.draw.rect(window, cboxColor, (210, 410, 100, 80))
    pygame.draw.rect(window, cboxColor, (410, 410, 100, 80))
    pygame.draw.rect(window, cboxColor, (610, 410, 100, 80))
    # Line7
    pygame.draw.rect(window, cboxColor, (110, 490, 100, 80))
    pygame.draw.rect(window, cboxColor, (310, 490, 100, 80))
    pygame.draw.rect(window, cboxColor, (510, 490, 100, 80))
    pygame.draw.rect(window, cboxColor, (710, 490, 100, 80))
    # line8
    pygame.draw.rect(window, cboxColor, (10, 570, 100, 80))
    pygame.draw.rect(window, cboxColor, (210, 570, 100, 80))
    pygame.draw.rect(window, cboxColor, (410, 570, 100, 80))
    pygame.draw.rect(window, cboxColor, (610, 570, 100, 80))

def placePieces():

    # Blacks Pieces Line1
    pygame.draw.circle(window, black, [160, 50], 40)
    pygame.draw.circle(window, liteblack, [160, 50], 20)
    pygame.draw.circle(window, black, [360, 50], 40)
    pygame.draw.circle(window, liteblack, [360, 50], 20)
    pygame.draw.circle(window, black, [560, 50], 40)
    pygame.draw.circle(window, liteblack, [560, 50], 20)
    pygame.draw.circle(window, black, [760, 50], 40)
    pygame.draw.circle(window, liteblack, [760, 50], 20)
    # line2
    pygame.draw.circle(window, black, [60, 130], 40)
    pygame.draw.circle(window, liteblack, [60, 130], 20)
    pygame.draw.circle(window, black, [260, 130], 40)
    pygame.draw.circle(window, liteblack, [260, 130], 20)
    pygame.draw.circle(window, black, [460, 130], 40)
    pygame.draw.circle(window, liteblack, [460, 130], 20)
    pygame.draw.circle(window, black, [660, 130], 40)
    pygame.draw.circle(window, liteblack, [660, 130], 20)
    # line3
    pygame.draw.circle(window, black, [160, 210], 40)
    pygame.draw.circle(window, liteblack, [160, 210], 20)
    pygame.draw.circle(window, black, [360, 210], 40)
    pygame.draw.circle(window, liteblack, [360, 210], 20)
    pygame.draw.circle(window, black, [560, 210], 40)
    pygame.draw.circle(window, liteblack, [560, 210], 20)
    pygame.draw.circle(window, black, [760, 210], 40)
    pygame.draw.circle(window, liteblack, [760, 210], 20)

    #white Pieces Line 1
    pygame.draw.circle(window, white, [60, 450], 40)
    pygame.draw.circle(window, litegrey, [60, 450], 20)
    pygame.draw.circle(window, white, [260, 450], 40)
    pygame.draw.circle(window, litegrey, [260, 450], 20)
    pygame.draw.circle(window, white, [460, 450], 40)
    pygame.draw.circle(window, litegrey, [460, 450], 20)
    pygame.draw.circle(window, white, [660, 450], 40)
    pygame.draw.circle(window, litegrey, [660, 450], 20)
    #line2
    pygame.draw.circle(window, white, [160, 530], 40)
    pygame.draw.circle(window, litegrey, [160, 530], 20)
    pygame.draw.circle(window, white, [360, 530], 40)
    pygame.draw.circle(window, litegrey, [360, 530], 20)
    pygame.draw.circle(window, white, [560, 530], 40)
    pygame.draw.circle(window, litegrey, [560, 530], 20)
    pygame.draw.circle(window, white, [760, 530], 40)
    pygame.draw.circle(window, litegrey, [760, 530], 20)
    #line3
    pygame.draw.circle(window, white, [60, 610], 40)
    pygame.draw.circle(window, litegrey, [60, 610], 20)
    pygame.draw.circle(window, white, [260, 610], 40)
    pygame.draw.circle(window, litegrey, [260, 610], 20)
    pygame.draw.circle(window, white, [460, 610], 40)
    pygame.draw.circle(window, litegrey, [460, 610], 20)
    pygame.draw.circle(window, white, [660, 610], 40)
    pygame.draw.circle(window, litegrey, [660, 610], 20)




if __name__ == '__main__':main()

