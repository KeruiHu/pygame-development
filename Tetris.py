import pygame, sys, random, time
from pygame.locals import *

pygame.init()

canvas_width = 320
canvas_height = 400
score_list = [0,10,30,60,100]

cubelist = ['I','J','L','O','S','T','Z']

DISPLAY = pygame.display.set_mode((canvas_width,canvas_height))

clock = pygame.time.Clock()

pygame.display.set_caption("Tetris")

defaultFont = pygame.font.SysFont("SIMYOU.TTF", 40)

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(150, 150, 150)
RED = pygame.Color(255, 0, 0)
"""
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
PURPLE = pygame.Color(255, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
LIGHTBLUE = pygame.Color(0, 255, 255)
ORANGE = pygame.Color(255, 128, 0)
"""
class Game:
    def __init__(self,level):
        self.level = level
        self.score = 0
        self.base = []
        self.checkBase = False
        self.isRun = True
        self.cubeLoc = []
        self.initLoc = [100,0]
        self.nextLoc = [250,160]
        self.nextcube = []
        self.cubeExist = False
        self.cubetype = ''
        self.rotatearound = []
        self.count = [0 for i in range(20)]

    def getcubetype(self):
        self.cubetype = random.choice(cubelist)

    def generateCube(self):
        ##self.cubetype = 'O'
        if self.cubetype == 'I':
            self.cubeLoc = [[self.initLoc[0]-20,self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0]+20,self.initLoc[1]],
                            [self.initLoc[0]+40,self.initLoc[1]]]
            self.cubeExist = True
            self.rotatearound = 3

        if self.cubetype == 'L':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]+20,self.initLoc[1]+20],
                            [self.initLoc[0]+40,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 2

        if self.cubetype == 'J':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]-20,self.initLoc[1]+20],
                            [self.initLoc[0]-40,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 1

        if self.cubetype == 'O':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0]+20,self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]+20,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 3

        if self.cubetype == 'S':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0]+20,self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]-20,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 2

        if self.cubetype == 'T':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]+20,self.initLoc[1]+20],
                            [self.initLoc[0]-20,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 1

        if self.cubetype == 'Z':
            self.cubeLoc = [[self.initLoc[0],self.initLoc[1]],
                            [self.initLoc[0]-20,self.initLoc[1]],
                            [self.initLoc[0],self.initLoc[1]+20],
                            [self.initLoc[0]+20,self.initLoc[1]+20]]
            self.cubeExist = True
            self.rotatearound = 3
        self.getcubetype()
    def drawcube(self):
        for x in self.cubeLoc:
            pygame.draw.rect(DISPLAY, WHITE, Rect(x[0], x[1], 18, 18))
        for x in self.base:
            pygame.draw.rect(DISPLAY, WHITE, Rect(x[0], x[1], 18, 18))

    def checkifscore(self):
        clearrow = []
        scorelevel = 0
        for row in range(20):
            if self.count[row] == 10:
                scorelevel = scorelevel+1
                for x in range(10):
                    pygame.draw.rect(DISPLAY, RED, Rect(x*20, row*20, 18, 18))
                self.count[row] = 0
                clearrow.append(row*20)
                temp = []
                for y in self.base:
                    if y[1] != row*20:
                        temp.append(y)
                self.base = temp
        pygame.display.update()
        if clearrow:
            time.sleep(0.2)

        for row in clearrow:
            temp = []
            for x in self.base:
                if x[1]<row:
                    temp.append([x[0],x[1]+20])
                    self.count[int(x[1]/20)] = self.count[int(x[1]/20)]-1
                    self.count[int(x[1]/20)+1] = self.count[int(x[1]/20)+1]+1
                else:
                    temp.append(x)
            self.base = temp
        for x in self.base:
            pygame.draw.rect(DISPLAY, WHITE, Rect(x[0], x[1], 18, 18))
        pygame.display.update()
        self.score = self.score + score_list[scorelevel]

    def showscore(self):
        Score_Surf = defaultFont.render('%s' %(self.score), True, GREY)
        score_Rect = Score_Surf.get_rect()
        score_Rect.midtop = (290, 330)
        DISPLAY.blit(Score_Surf, score_Rect)
        pygame.display.update()

    def drawframe(self):
        Score_Surf = defaultFont.render('%s' %('Score:'), True, GREY)
        score_Rect = Score_Surf.get_rect()
        score_Rect.midtop = (250, 260)
        DISPLAY.blit(Score_Surf, score_Rect)
        Score_Surf2 = defaultFont.render('%s' %('Next:'), True, GREY)
        score_Rect2 = Score_Surf2.get_rect()
        score_Rect2.midtop = (240, 75)
        DISPLAY.blit(Score_Surf2, score_Rect2)
        for x in range(canvas_height):
            pygame.draw.rect(DISPLAY, WHITE, Rect(202, x, 2, 2))
        pygame.display.update()

    def drawnext(self):
        if self.cubetype == 'I':
            self.nextcube = [[self.nextLoc[0]-25,self.nextLoc[1]],
                            [self.nextLoc[0]-5,self.nextLoc[1]],
                            [self.nextLoc[0]+15,self.nextLoc[1]],
                            [self.nextLoc[0]+35,self.nextLoc[1]]]

        if self.cubetype == 'L':
            self.nextcube = [[self.nextLoc[0]-20,self.nextLoc[1]],
                            [self.nextLoc[0]-20,self.nextLoc[1]+20],
                            [self.nextLoc[0],self.nextLoc[1]+20],
                            [self.nextLoc[0]+20,self.nextLoc[1]+20]]

        if self.cubetype == 'J':
            self.nextcube = [[self.nextLoc[0]+20,self.nextLoc[1]],
                            [self.nextLoc[0]+20,self.nextLoc[1]+20],
                            [self.nextLoc[0],self.nextLoc[1]+20],
                            [self.nextLoc[0]-20,self.nextLoc[1]+20]]

        if self.cubetype == 'O':
            self.nextcube = [[self.nextLoc[0]-10,self.nextLoc[1]],
                            [self.nextLoc[0]+10,self.nextLoc[1]],
                            [self.nextLoc[0]-10,self.nextLoc[1]+20],
                            [self.nextLoc[0]+10,self.nextLoc[1]+20]]

        if self.cubetype == 'S':
            self.nextcube = [[self.nextLoc[0],self.nextLoc[1]],
                            [self.nextLoc[0]+20,self.nextLoc[1]],
                            [self.nextLoc[0],self.nextLoc[1]+20],
                            [self.nextLoc[0]-20,self.nextLoc[1]+20]]

        if self.cubetype == 'T':
            self.nextcube = [[self.nextLoc[0],self.nextLoc[1]],
                            [self.nextLoc[0],self.nextLoc[1]+20],
                            [self.nextLoc[0]+20,self.nextLoc[1]+20],
                            [self.nextLoc[0]-20,self.nextLoc[1]+20]]

        if self.cubetype == 'Z':
            self.nextcube = [[self.nextLoc[0],self.nextLoc[1]],
                            [self.nextLoc[0]-20,self.nextLoc[1]],
                            [self.nextLoc[0],self.nextLoc[1]+20],
                            [self.nextLoc[0]+20,self.nextLoc[1]+20]]

        for x in self.nextcube:
            pygame.draw.rect(DISPLAY, WHITE, Rect(x[0], x[1], 18, 18))
        pygame.display.update()

    def GameOver(self):
        GameOver_Surf = defaultFont.render('Game Over!(R/Q)', True, GREY)
        GameOver_Rect = GameOver_Surf.get_rect()
        GameOver_Rect.midtop = (100, 20)
        DISPLAY.blit(GameOver_Surf, GameOver_Rect)

        pygame.display.flip()
        time.sleep(3)
        self.isRun = False
        pygame.quit()
        sys.exit()

    def run(self):
        self.getcubetype()
        self.generateCube()
        self.cubeExist = True
        while self.isRun:
            clock.tick(self.level)
            if not self.cubeExist:
                self.generateCube()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    self.isRun = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if(event.key == K_LEFT):
                        doable = True
                        for x in self.cubeLoc:
                            if x[0]-20<0 or [x[0]-20,x[1]] in self.base:
                                doable = False
                        if doable:
                            self.cubeLoc = [[i[0]-20,i[1]] for i in self.cubeLoc]
                        self.drawcube()
                        pygame.display.update()

                    if(event.key == K_RIGHT):
                        doable = True
                        for x in self.cubeLoc:
                            if x[0]+20>180 or [x[0]+20,x[1]] in self.base:
                                doable = False
                        if doable:
                            self.cubeLoc = [[i[0]+20,i[1]] for i in self.cubeLoc]
                        self.drawcube()
                        pygame.display.update()

                    if(event.key == K_DOWN):
                        oable = True
                        for x in self.cubeLoc:
                            if x[1]+20>380 or [x[0],x[1]+20] in self.base:
                                doable = False
                        if doable:
                            self.cubeLoc = [[i[0],i[1]+20] for i in self.cubeLoc]
                        self.drawcube()
                        pygame.display.update()

                    if(event.key == K_UP):
                        doable = True
                        originx = self.cubeLoc[self.rotatearound][0]
                        originy = self.cubeLoc[self.rotatearound][1]
                        for x in self.cubeLoc:
                            if x[1] - originy + originx > 180 or x[1] - originy + originx < 0 or originy + originx - x[0] > 380 or originy + originx - x[0] < 0 or [x[1] - originy + originx , originy + originx - x[0]] in self.base:
                                doable = False
                        if doable:
                            self.cubeLoc = [[i[1] - originy + originx , originy + originx - i[0]] for i in self.cubeLoc]
                        self.drawcube()
                        pygame.display.update()


            doable = True
            for x in self.cubeLoc:
                if x[1]+20>380 or [x[0],x[1]+20] in self.base:
                    doable = False
            if doable:
                self.cubeLoc = [[i[0],i[1]+20] for i in self.cubeLoc]
            else:
                for x in self.cubeLoc:
                    self.base.append(x)
                    self.count[int(x[1]/20)]=self.count[int(x[1]/20)]+1
                self.cubeExist = False
                self.cubeLoc = []

            DISPLAY.fill(BLACK)
            self.drawcube()
            self.drawframe()
            self.drawnext()
            pygame.display.update()

            self.checkifscore()
            self.showscore()

            for x in self.base:
                if x[1]<=0:
                    self.GameOver()





def main():
    theGame = Game(4)
    print("game begin!!")
    theGame.run()
    print("game end.")

if __name__ == "__main__":
    main()
