# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 		ROLANDO JIMENEZ
#               SAFERA RANA
# 	 		    AUSTIN JOHN
#			    Bailey LaMotte 
# Section:		ENGR 102- 506
# Assignment:	PYGAME PROGRAM | PROJECT
# Date:		    5TH December, 2019
import pygame
from pygame.locals import*
from random import randint

pygame.init()
#######MUSIC ON REPEAT##############
pygame.mixer.music.load('techological.mp3')
pygame.mixer.music.play(-1)
############## GAME DISPLAY SIZE ###########
display_width = 600
display_height = 600
game_display = pygame.display.set_mode((display_width,display_height))
############# BACKGROUND IMAGE #############
bg = pygame.image.load('trouble.jpg') 
p1 = pygame.image.load('Player1.png')
p2 = pygame.image.load('Player2.png')
pp1 = pygame.image.load('Piece1.png')
pp2 = pygame.image.load('Piece2.png')
pp3 = pygame.image.load('Piece3.png')
pp4 = pygame.image.load('Piece4.png')
############# GAMAE ICON   ################
icon = pygame.image.load('pawn.png')
pygame.display.set_icon(icon)
######## TITLE OF THE GAME #################
pygame.display.set_caption("TROUBLE")
############ BOARD POSSITIONS #############
pieceX = ['a','b','c','d']
pieceY = ['e','f','g','h']
homeX = [102,80,61,45]
homeY = [450,433,413,393]
posX = [88,67,53,50,50,50,50,50,54,69,90,116,139,168,195,220,248,276,304,328,350,
        376,389,392,393,392,392,392,382,373,353,325,302,274,249,220,193,165,140,
        120]
posY = [400,373,350,322,300,270,240,215,188,163,140,116,105,100,100,100,100,101,107,
        120,140,170,190,220,250,275,301,330,356,378,400,425,437,441,440,440,440,443,438,420]
finishX = 112
finishY = 381
EfinishX = 330
EfinishY = 165
EpieceX = ['r','t','u','v']
EpieceY = ['w','x','y','z']
EhomeX = [340,363,380,396]
EhomeY = [92,109,130,150]
EposX = [350,376,389,392,393,392,392,392,382,373,353,325,302,274,249,220,193,165,140,
        120,67,53,50,50,50,50,50,54,69,90,116,139,168,195,220,248,276,304,328]
EposY = [140,170,190,220,250,275,301,330,356,378,400,425,437,441,440,440,440,443,438,420,
         373,350,322,300,270,240,215,188,163,140,116,105,100,100,100,100,101,107,
        120]
EfinishX = 330
EfinishY = 165
Step = [False,False,False,False]
'''
Step1 = False
Step2 = False
Step3 = False
Step4 = False
'''
EStep = [False,False,False,False]
'''
EStep1 = False
EStep2 = False
EStep3 = False
EStep4 = False
'''
end1 = False
end2 = False
end3 = False
end4 = False

End1 = False
End2 = False
End3 = False
End4 = False

 
piece1 = False
piece2 = False
piece3 = False
piece4 = False

player1 = True
player2 = False
########### PLAYER 1 #############
n = 0
o = 0 
p = 0
q = 0
i = 0
playerImg = pygame.image.load('newduck.png')

pieceX[0] = homeX[0]
pieceY[0] = homeY[0]
playerX_change = 0 ### OUR MOVEMENT  | VELOCITY PER PIXLE
playerY_change = 0 ### OUR MOVEMENT  | VELOCITY PER PIXLE 

pieceX[1] = homeX[1]
pieceY[1] = homeY[1]

pieceX[2] = homeX[2]
pieceY[2] = homeY[2]

pieceX[3] = homeX[3]
pieceY[3] = homeY[3]

############ PLAYER 2 #################
j = 0
k = 0
l = 0 
m = 0
enemyImg = pygame.image.load('newdog.png')
EpieceX[0] = EhomeX[0]
EpieceY[0] = EhomeY[0]

EpieceX[1] = EhomeX[1]
EpieceY[1] = EhomeY[1]

EpieceX[2] = EhomeX[2]
EpieceY[2] = EhomeY[2]

EpieceX[3] = EhomeX[3]
EpieceY[3] = EhomeY[3]
############PLAYER FUNCTION###########
def player(x,y):
    ## THIS WILL DRAW | BLIT MEANS TO DRAW #####
    game_display.blit(playerImg, (x-6, y-6))
    ## THIS WILL DRAW ENEMY | BLIT MEANS TO DRAW ##
def enemy(x,y):
    game_display.blit(enemyImg, (x-6, y-6))


def draw_loop():
    #######RGB VALUE (red,green,blue) ###
    game_display.fill((255,255,255))
    ##### MUST CALL PLAYER FUNCTION BEFORE FILL BECUASE WE NEED PLAYER TO BE 
    ##### ABOVE OUR BACKGROUND IMAGE ##############
    game_display.blit(bg, (0,0))
    if player1 == True:
        game_display.blit(p1, (500,100))
    if player2 == True:
        game_display.blit(p2, (500,100))
    if piece1 == True:
        game_display.blit(pp1, (400,200))
    if piece2 == True:
        game_display.blit(pp2, (400,200))
    if piece3 == True:
        game_display.blit(pp3, (400,200)) 
    if piece4 == True:
        game_display.blit(pp4, (400,200))
    player(pieceX[0], pieceY[0])
    player(pieceX[1], pieceY[1])
    player(pieceX[2], pieceY[2])
    player(pieceX[3], pieceY[3])
    #### ENEMY PLAYER BEING DRAWN #####
    enemy(EpieceX[0], EpieceY[0])
    enemy(EpieceX[1], EpieceY[1])
    enemy(EpieceX[2], EpieceY[2])
    enemy(EpieceX[3], EpieceY[3])
    pygame.display.update()##REFRESH PIXLES##

#### RANDOM NUM GEN #####
def random_num():
    global value
    global num
    value = randint(1,6)
    num = randint(-1,1)
    print("Dice Rolled")
    print("VALUE:",value)
    return value and num
    
    
while True:######M#########MAIN CODE LOOP #########
    #draw_loop()#### INITIATE DRAW FUNCTION #######
    for event in pygame.event.get():
        #print(event)
        #### QUIT THROUGH KEYS ###
        if event.type == QUIT or (
                event.type == pygame.KEYDOWN and ( 
                        event.key == K_ESCAPE or
                        event.key == K_q
                        )):
            pygame.quit()
            quit()
        ### DOES SOMETHING IF KEY: ENTER IS PRESSED##
        if event.type == pygame.KEYDOWN:
################################################## PLAYER 1 ##########################################
            if player1 == True:
                ### RUN PLAYER 1 CODE
                print("########PLAYER 1 MAKE YOUR MOVE########") ## WILL ADD IMAGE LATER
                if event.key == K_1:
                    i = 0
                    piece1 = True
                    piece2 = False
                    piece3 = False
                    piece4 = False
                    print("PIECE 1 has been selected")
                elif event.key == K_2:
                    i = 1
                    piece1 = False
                    piece2 = True
                    piece3 = False
                    piece4 = False
                    print("PIECE 2 Has been selected")
                elif event.key == K_3:
                    i = 2
                    piece1 = False
                    piece2 = False
                    piece3 = True
                    piece4 = False
                    print("PIECE 3 Has been selected")
                elif event.key == K_4:
                    i = 3
                    piece1 = False
                    piece2 = False
                    piece3 = False   
                    piece4 = True
                    print("PIECE 4 Has been selected")
                if Step[i] == False and (piece1 != False) and (event.key == K_RETURN) and i == 0 and end1 == False:##### PIECE 1 ####
                    random_num()
                    i = 0 
                    if value!=6 and (player(pieceX[i],pieceY[i]) == player(homeX[0],homeY[0])):
                            print("CANNOT MOVE PIECE 1")
                            print("PLAYER'S 2 TURN!!!!!!")
                            print("X",pieceX[i])
                            print("Y",pieceY[i])
                            print("N",n)  
                            player1 = False ######### SWITCHES TO PLAYER 2 BECUASE P1 Just ROLLED
                            player2 = True
                    elif value == 6 and (player(pieceX[i],pieceY[i]) == player(homeX[0],homeY[0])):
                            pieceX[i] = posX[0] #### START POSITION ####
                            pieceY[i] = posY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            n += value
                            pieceX[i] = posX[n]
                            pieceY[i] = posY[n]
                            Step[i] = True 
                            print("N:",n)
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                            
                elif Step[i] == True and (piece1 != False) and (event.key == K_RETURN) and i == 0 and end1 == False:
                    random_num()  
                    i = 0 
                    n += value
                    if n >= 39:
                        ############ END GAME
                        pieceX[i] = finishX
                        pieceY[i] = finishY
                        end1 = True
                    elif player(pieceX[i],pieceY[i]) == player(posX[n],posY[n]):
                        #
                        print("ONCE ON THE BOARD 1 SHOULD MOVE")
                        pieceX[i] = posX[n]
                        pieceY[i] = posY[n]
                        print("N:",n)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            n += value
                            if n >= 39: ############ END GAME
                                pieceX[i] = finishX
                                pieceY[i] = finishY
                                end1 = True    
                            else:
                                    
                                pieceX[i] = posX[n]
                                pieceY[i] = posY[n]
                                print("N:",n)
                                player1 = False
                                player2 = True
                                print("PLAYER'S 2 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                        
                if Step[i] == False and (piece2 != False) and (event.key == K_RETURN) and i == 1: ### PIECE 2 ###
                    random_num()
                    i = 1
                    if value!=6 and (player(pieceX[i],pieceY[i]) == player(homeX[1],homeY[1])):
                            print("CANNOT MOVE PIECE 2")
                            print("PLAYER'S 2 TURN!!!!!!")
                            print("X",pieceX[i])
                            print("Y",pieceY[i])
                            print("O",o)  
                            player1 = False
                            player2 = True
                    elif value == 6 and (player(pieceX[i],pieceY[i]) == player(homeX[1],homeY[1])):
                            pieceX[i] = posX[0] #### START POSITION ####
                            pieceY[i] = posY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            o += value
                            pieceX[i] = posX[o]
                            pieceY[i] = posY[o]
                            Step[i] = True 
                            print("O:",o)
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                elif Step[i] == True and (piece2 != False) and (event.key == K_RETURN) and i == 1 and end2 == False:
                    random_num()  
                    i = 1 
                    o += value
                    if o >= 39:
                        ############ END GAME
                        pieceX[i] = finishX
                        pieceY[i] = finishY
                        end2 = True
                    elif player(pieceX[i],pieceY[i]) == player(posX[o],posY[o]):
                        #
                        print("ONCE ON THE BOARD 2 SHOULD MOVE")
                        pieceX[i] = posX[o]
                        pieceY[i] = posY[o]
                        print("O:",o)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            o += value
                            if o >= 39: ############ END GAME
                                pieceX[i] = finishX
                                pieceY[i] = finishY
                                end2 = True    
                            else:
                                    
                                pieceX[i] = posX[o]
                                pieceY[i] = posY[o]
                                print("O:",o)
                                player1 = False
                                player2 = True
                                print("PLAYER'S 2 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                        
                if Step[i] == False and (piece3 != False) and (event.key == K_RETURN) and i == 2: ### PIECE 3 ###
                    random_num()
                    i = 2
                    if value!=6 and (player(pieceX[i],pieceY[i]) == player(homeX[2],homeY[2])):
                            print("CANNOT MOVE PIECE 3")
                            print("PLAYER'S 2 TURN!!!!!!")
                            print("X",pieceX[i])
                            print("Y",pieceY[i])
                            print("p",p)        
                            player1 = False
                            player2 = True
                    elif value == 6 and (player(pieceX[i],pieceY[i]) == player(homeX[2],homeY[2])):
                            pieceX[i] = posX[0] #### START POSITION ####
                            pieceY[i] = posY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            p += value
                            pieceX[i] = posX[p]
                            pieceY[i] = posY[p]
                            Step[i] = True 
                            print("P:",p)
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                elif Step[i] == True and (piece3 != False) and (event.key == K_RETURN) and i == 2 and end3 == False:
                    random_num()  
                    i = 2
                    p += value
                    if p >= 39:
                        ############ END GAME
                        pieceX[i] = finishX
                        pieceY[i] = finishY
                        end1 = True
                    elif player(pieceX[i],pieceY[i]) == player(posX[p],posY[p]):
                        #
                        print("ONCE ON THE BOARD 3 SHOULD MOVE")
                        pieceX[i] = posX[p]
                        pieceY[i] = posY[p]
                        print("P:",p)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            p += value
                            if p >= 39: ############ END GAME
                                pieceX[i] = finishX
                                pieceY[i] = finishY
                                end3 = True    
                            else:
                                    
                                pieceX[i] = posX[p]
                                pieceY[i] = posY[p]
                                print("P:",p)
                                player1 = False
                                player2 = True
                                print("PLAYER'S 2 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                        
                if Step[i] == False and (piece4 != False) and (event.key == K_RETURN) and i == 3: ### PIECE 4 
                    random_num()
                    i = 3
                    if value!=6 and (player(pieceX[i],pieceY[i]) == player(homeX[3],homeY[3])):
                            print("CANNOT MOVE PIECE 4")
                            print("PLAYER'S 2 TURN!!!!!!")
                            print("X",pieceX[i])
                            print("Y",pieceY[i])
                            print("q",q)        
                            player1 = False
                            player2 = True
                    elif value == 6 and (player(pieceX[i],pieceY[i]) == player(homeX[3],homeY[3])):
                            pieceX[i] = posX[0] #### START POSITION ####
                            pieceY[i] = posY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            q += value
                            pieceX[i] = posX[q]
                            pieceY[i] = posY[q]
                            Step[i] = True 
                            print("Q:",q)
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                elif Step[i] == True and (piece4 != False) and (event.key == K_RETURN) and i == 3 and end4 == False:
                    random_num()  
                    i = 3 
                    q += value
                    if q >= 39:
                        ############ END GAME
                        pieceX[i] = finishX
                        pieceY[i] = finishY
                        end4 = True
                    elif player(pieceX[i],pieceY[i]) == player(posX[q],posY[q]):
                        #
                        print("ONCE ON THE BOARD 4 SHOULD MOVE")
                        pieceX[i] = posX[q]
                        pieceY[i] = posY[q]
                        print("N:",n)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            n += value
                            if q >= 39: ############ END GAME
                                pieceX[i] = finishX
                                pieceY[i] = finishY
                                end4 = True    
                            else:
                                    
                                pieceX[i] = posX[q]
                                pieceY[i] = posY[q]
                                print("Q:",q)
                                player1 = False
                                player2 = True
                                print("PLAYER'S 2 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = False
                            player2 = True
                            print("PLAYER'S 2 TURN!!!!!!")
                        
                for d in range(4):   
                    for e in range(4):
                        if  pieceX[d] == EpieceX[e] and (pieceY[d] == EpieceY[e]):
                            print("WHOOPS!!! Piece",e+1,"GO HOME!!")
                            print("PLAYER",pieceX[d],pieceY[d])
                            print("ENEMY:",EpieceX[e],EpieceY[e])
                            EpieceX[e] = EhomeX[e]
                            EpieceY[e] = EhomeY[e]
                            EStep[e] = False
                            if EStep[e] == False and d == 0:
                                j = 0
                            elif EStep[e] == False and d == 1:
                                k = 0
                            elif EStep[e] == False and d == 2:
                                l = 0
                            elif EStep[e] == False and d == 3:
                                m = 0
                if pieceX[0] == finishX and pieceX[1] == finishX and pieceX[2] == finishX and pieceX[3] == finishX:
                    player2 = False
                    print("YOU WIN")
                                
                        

                    
                                
######################################## PLAYER 2 ##############################################################
            elif player2 == True:
                ### RUN PLAYER 2 CODE
                print("PLAYER 2 MAKE YOUR MOVE") ## WILL ADD IMAGE LATER
                if event.key == K_1:
                    i = 0
                    piece1 = True
                    piece2 = False
                    piece3 = False
                    piece4 = False
                    print("PIECE 1 has been selected")
                elif event.key == K_2:
                    i = 1
                    piece1 = False
                    piece2 = True
                    piece3 = False
                    piece4 = False
                    print("PIECE 2 Has been selected")
                elif event.key == K_3:
                    i = 2
                    piece1 = False
                    piece2 = False
                    piece3 = True
                    piece4 = False
                    print("PIECE 3 Has been selected")
                elif event.key == K_4:
                    i = 3
                    piece1 = False
                    piece2 = False
                    piece3 = False   
                    piece4 = True
                    print("PIECE 4 Has been selected")
                if EStep[i] == False and (piece1 != False) and (event.key == K_RETURN) and i == 0 and End1 == False:##### PIECE 1 ####
                    random_num()
                    i = 0 
                    if value!=6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[0],EhomeY[0])):
                            print("CANNOT MOVE PIECE 1")
                            print("Player's 1 turn")
                            print("X",EpieceX[i])
                            print("Y",EpieceY[i])
                            print("J",j)
                            player1 = True
                            player2 = False
                    elif value == 6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[0],EhomeY[0])):
                            EpieceX[i] = EposX[0] #### START POSITION ####
                            EpieceY[i] = EposY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            j += value
                            EpieceX[i] = EposX[j]
                            EpieceY[i] = EposY[j]
                            EStep[i] = True 
                            print("J:",j)
                            player1 = True
                            player2 = False
                            print("Player's 1 turn")
                            
                elif EStep[i] == True and (piece1 != False) and (event.key == K_RETURN) and i == 0 and End1 == False:
                    random_num()  
                    i = 0 
                    j += value
                    if j >= 39:
                        ############ END GAME
                        EpieceX[i] = EfinishX
                        EpieceY[i] = EfinishY
                        End1 = True
                    elif enemy(EpieceX[i],EpieceY[i]) == enemy(EposX[j],EposY[j]):
                        #
                        print("ONCE ON THE BOARD 1 SHOULD MOVE")
                        EpieceX[i] = EposX[j]
                        EpieceY[i] = EposY[j]
                        print("J:",j)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            j += value
                            if j >= 39: ############ END GAME
                                EpieceX[i] = EfinishX
                                EpieceY[i] = EfinishY
                                End1 = True    
                            else:
                                    
                                EpieceX[i] = EposX[j]
                                EpieceY[i] = EposY[j]
                                print("J:",j)
                                player1 = True
                                player2 = False
                                print("PLAYER'S 1 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = True
                            player2 = False
                            print("PLAYER'S 1 TURN!!!!!!")
                        
                if EStep[i] == False and (piece2 != False) and (event.key == K_RETURN) and i == 1: ### PIECE 2 ###
                    random_num()
                    i = 1
                    if value!=6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[1],EhomeY[1])):
                            print("CANNOT MOVE PIECE 2")
                            print("Player's 1 turn")
                            print("X",EpieceX[i])
                            print("Y",EpieceY[i])
                            print("K",k)        
                            player1 = True
                            player2 = False
                    elif value == 6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[1],EhomeY[1])):
                            EpieceX[i] = posX[0] #### START POSITION ####
                            EpieceY[i] = posY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            k += value
                            EpieceX[i] = EposX[k]
                            EpieceY[i] = EposY[k]
                            EStep[i] = True 
                            print("K:",k)
                            player1 = True
                            player2 = False
                            print("Player's 1 turn")
                elif EStep[i] == True and (piece2 != False) and (event.key == K_RETURN) and i == 1 and End2 == False:
                    random_num()  
                    i = 1 
                    k += value
                    if k >= 39:
                        ############ END GAME
                        EpieceX[i] = EfinishX
                        EpieceY[i] = EfinishY
                        End2 = True
                    elif enemy(EpieceX[i],EpieceY[i]) == enemy(EposX[k],EposY[k]):
                        #
                        print("ONCE ON THE BOARD 1 SHOULD MOVE")
                        EpieceX[i] = EposX[k]
                        EpieceY[i] = EposY[k]
                        print("k:",k)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            k += value
                            if k >= 39: ############ END GAME
                                EpieceX[i] = EfinishX
                                EpieceY[i] = EfinishY
                                End1 = True    
                            else:
                                    
                                EpieceX[i] = EposX[k]
                                EpieceY[i] = EposY[k]
                                print("k:",k)
                                player1 = True
                                player2 = False
                                print("PLAYER'S 1 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = True
                            player2 = False
                            print("PLAYER'S 1 TURN!!!!!!")
                        
                if EStep[i] == False and (piece3 != False) and (event.key == K_RETURN) and i == 2: ### PIECE 3 ###
                    random_num()
                    i = 2
                    if value!=6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[2],EhomeY[2])):
                            print("CANNOT MOVE PIECE 3")
                            print("Player's 1 turn")
                            print("X",EpieceX[i])
                            print("Y",EpieceY[i])
                            print("L",l)        
                            player1 = True
                            player2 = False
                    elif value == 6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[2],EhomeY[2])):
                            EpieceX[i] = EposX[0] #### START POSITION ####
                            EpieceY[i] = EposY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            l += value
                            EpieceX[i] = EposX[l]
                            EpieceY[i] = EposY[l]
                            EStep[i] = True 
                            print("L:",l)
                            player1 = True
                            player2 = False
                            print("Player's 1 turn")
                elif EStep[i] == True and (piece3 != False) and (event.key == K_RETURN) and i == 2 and End3 == False:
                    random_num()  
                    i = 2
                    l += value
                    if l >= 39:
                        ############ END GAME
                        EpieceX[i] = EfinishX
                        EpieceY[i] = EfinishY
                        End3 = True
                    elif enemy(EpieceX[i],EpieceY[i]) == enemy(EposX[l],EposY[l]):
                        #
                        print("ONCE ON THE BOARD 3 SHOULD MOVE")
                        EpieceX[i] = EposX[l]
                        EpieceY[i] = EposY[l]
                        print("l:",l)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            l += value
                            if l >= 39: ############ END GAME
                                EpieceX[i] = EfinishX
                                EpieceY[i] = EfinishY
                                End3 = True    
                            else:
                                    
                                EpieceX[i] = EposX[l]
                                EpieceY[i] = EposY[l]
                                print("l:",l)
                                player1 = True
                                player2 = False
                                print("PLAYER'S 1 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = True
                            player2 = False
                            print("PLAYER'S 1 TURN!!!!!!")
                if EStep[i] == False and (piece4 != False) and (event.key == K_RETURN) and i == 3: ### PIECE 4 
                    random_num()
                    i = 3
                    if value!=6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[3],EhomeY[3])):
                            print("CANNOT MOVE PIECE 4")
                            print("Player's 1 turn")
                            print("X",EpieceX[i])
                            print("Y",EpieceY[i])
                            print("M",m)        
                            player1 = True
                            player2 = False
                    elif value == 6 and (enemy(EpieceX[i],EpieceY[i]) == enemy(EhomeX[3],EhomeY[3])):
                            EpieceX[i] = EposX[0] #### START POSITION ####
                            EpieceY[i] = EposY[0]
                            print("YOU WILL ROOL AGAIN")
                            random_num()
                            m += value
                            EpieceX[i] = EposX[m]
                            EpieceY[i] = EposY[m]
                            EStep[i] = True 
                            print("M:",m)
                            player1 = True
                            player2 = False
                            print("Player's 1 turn")
                elif EStep[i] == True and (piece4 != False) and (event.key == K_RETURN) and i == 3 and End4 == False:
                    random_num()  
                    i = 3 
                    m += value
                    if m >= 39:
                        ############ END GAME
                        EpieceX[i] = EfinishX
                        EpieceY[i] = EfinishY
                        End4 = True
                    elif enemy(EpieceX[i],EpieceY[i]) == enemy(EposX[m],EposY[m]):
                        #
                        print("ONCE ON THE BOARD 4 SHOULD MOVE")
                        EpieceX[i] = EposX[m]
                        EpieceY[i] = EposY[m]
                        print("m:",m)
                        
                        if value == 6:
                            print("YOU GET TO ROLL AGAIN")
                            random_num()
                            m += value
                            if m >= 39: ############ END GAME
                                EpieceX[i] = EfinishX
                                EpieceY[i] = EfinishY
                                End4 = True    
                            else:
                                    
                                EpieceX[i] = EposX[m]
                                EpieceY[i] = EposY[m]
                                print("m:",m)
                                player1 = True
                                player2 = False
                                print("PLAYER'S 1 TURN!!!!!!")
                             
                        elif value !=6:
                            player1 = True
                            player2 = False
                            print("PLAYER'S 1 TURN!!!!!!")
                        
                for d in range(4):   
                    for e in range(4):
                        if  EpieceX[d] == pieceX[e] and (EpieceY[d] == pieceY[e]):
                            print("ENEMY",EpieceX[d],EpieceY[d])
                            print("PLAYER",pieceX[e],pieceY[e])
                            print("WHOOPS!!! Piece",e+1,"GO HOME!!")
                            pieceX[e] = homeX[e]
                            pieceY[e] = homeY[e]
                            Step[e] = False
                            if Step[e] == False and e == 0:
                                n = 0
                            elif Step[e] == False and e == 1:
                                o = 0
                            elif Step[e] == False and e == 2:
                                p = 0
                            elif Step[e] == False and e == 3:
                                q = 0    
                if EpieceX[0] == EfinishX and EpieceX[1] == EfinishX and EpieceX[2] == EfinishX and EpieceX[3] == EfinishX:
                     player1 = False 
                     print("YOU WIN")
                
    pieceX[i] += playerX_change
    pieceY[i] += playerY_change 
    ### ENEMY PLAYER ###
    EpieceX[i] += playerX_change
    EpieceY[i] += playerY_change
    n += 0
    o += 0
    p += 0 
    q += 0
    j += 0 
    k += 0
    l += 0
    m += 0
    
    draw_loop() ### DRAWING function##
    
    