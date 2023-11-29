import pygame
from pygame.locals import *

class WriteLetter:

    def __init__(self, surface):
        self.color = pygame.Color("Black")
        self.bumper = surface.get_height() / 10
        self.x = surface.get_width() + 10
        self.space = 0

    def drawA(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + 105 + space, 0 + self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)
        pygame.draw.line(surface, self.color, [self.x + 55 + space, surface.get_height() / 2],
                         [self.x + 150 + space, surface.get_height() / 2], 20)

    def drawB(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 152.5 + space, self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .25],
                                                       [self.x + 200 + space, surface.get_height() / 2 - 50],
                                                       [self.x + 152.5 + space, surface.get_height() / 2],
                                                       [self.x + space, surface.get_height() / 2],
                                                       [self.x + 152.5 + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, surface.get_height() / 2 + 50],
                                                       [self.x + 200 + space, surface.get_height() * .75],
                                                       [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + space, surface.get_height() - self.bumper]], 20)

    def drawC(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + 200 + space, self.bumper],
                                                       [self.x + 47.5 + space, self.bumper],
                                                       [self.x + space, surface.get_height() * .25],
                                                       [self.x + space, surface.get_height() * .75],
                                                       [self.x + 47.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawD(self, surface, space):
        pygame.draw.lines(surface, self.color, True, [[self.x + space, self.bumper],
                                                      [self.x + 152.5 + space, self.bumper],
                                                      [self.x + 200 + space, surface.get_height() * .25],
                                                      [self.x + 200 + space, surface.get_height() * .75],
                                                      [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                      [self.x + space, surface.get_height() - self.bumper]], 20)

    def drawE(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() / 2],
                         [self.x + 105 + space, surface.get_height() / 2], 20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() - self.bumper],
                         [self.x + 200 + space, surface.get_height() - self.bumper], 20)

    def drawF(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() / 2],
                         [self.x + 105 + space, surface.get_height() / 2], 20)

    def drawG(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + 200 + space, self.bumper],
                                                       [self.x + 47.5 + space, self.bumper],
                                                       [self.x + space, surface.get_height() * .25],
                                                       [self.x + space, surface.get_height() * .75],
                                                       [self.x + 47.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .75],
                                                       [self.x + 200 + space, surface.get_height() / 2],
                                                       [self.x + 105 + space, surface.get_height() / 2]], 20)

    def drawH(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() / 2],
                         [self.x + 200 + space, surface.get_height() / 2], 20)
        pygame.draw.line(surface, self.color, [self.x + 200 + space, surface.get_height() - self.bumper],
                         [self.x + 200 + space, self.bumper], 20)

    def drawI(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() - self.bumper],
                         [self.x + 200 + space, surface.get_height() - self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + 105 + space, self.bumper],
                         [self.x + 105 + space, surface.get_height() - self.bumper], 20)

    def drawJ(self, surface, space):
        # draws the top line of J
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, self.bumper], 20)
        # draws the hook part of the J
        pygame.draw.lines(surface, self.color, False, [[self.x + 105 + space, self.bumper],
                                                       [self.x + 105 + space, surface.get_height() - self.bumper],
                                                       [self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + space, surface.get_height() / 2]], 20)

    def drawK(self, surface, space):
        # draws the vertical line of the K
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        # draws the < part of the K
        pygame.draw.lines(surface, self.color, False, [[self.x + 200 + space, self.bumper],
                                                       [self.x + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawL(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawM(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + space, self.bumper],
                                                       [self.x + 105 + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawN(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + space, self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, self.bumper]], 20)

    def drawO(self, surface, space):
        # creates the whole circle that the O is
        pygame.draw.lines(surface, self.color, True, [[self.x + 47.5 + space, self.bumper],
                                                      [self.x + 152.5 + space, self.bumper],
                                                      [self.x + 200 + space, surface.get_height() * .25],
                                                      [self.x + 200 + space, surface.get_height() * .75],
                                                      [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                      [self.x + 47.5 + space, surface.get_height() - self.bumper],
                                                      [self.x + space, surface.get_height() * .75],
                                                      [self.x + space, surface.get_height() * .25]], 20)

    def drawP(self, surface, space):
        # draws the vertical line on the left side of the P
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        # draws the rounded portion of the P
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 152.5 + space, self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .25],
                                                       [self.x + 200 + space, surface.get_height() / 2 + -50],
                                                       [self.x + 152.5 + space, surface.get_height() / 2],
                                                       [self.x + space, surface.get_height() / 2]], 20)

    def drawQ(self, surface, space):
        # draws the circle along the outside of the Q
        pygame.draw.lines(surface, self.color, True, [[self.x + 47.5 + space, self.bumper],
                                                      [self.x + 152.5 + space, self.bumper],
                                                      [self.x + 200 + space, surface.get_height() * .25],
                                                      [self.x + 200 + space, surface.get_height() * .75],
                                                      [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                      [self.x + 47.5 + space, surface.get_height() - self.bumper],
                                                      [self.x + space, surface.get_height() * .75],
                                                      [self.x + space, surface.get_height() * .25]], 20)
        # draws the line going from the middle to the bottom right corner of the Q
        pygame.draw.line(surface, self.color, [self.x + 105 + space, surface.get_height() / 2],
                         [self.x + 200 + space, surface.get_height() - self.bumper], 20)

    def drawR(self,surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + space, surface.get_height() - self.bumper], 20)
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 152.5 + space, self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .25],
                                                       [self.x + 200 + space, surface.get_height() / 2 + -50],
                                                       [self.x + 152.5 + space, surface.get_height() / 2],
                                                       [self.x + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawS(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + 152.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .75],
                                                       [self.x + 200 + space, surface.get_height() / 2 + 50],
                                                       [self.x + 152.5 + space, surface.get_height() / 2],
                                                       [self.x + 47.5 + space, surface.get_height() / 2],
                                                       [self.x + space, surface.get_height() / 2 - 50],
                                                       [self.x + space, surface.get_height() * .25],
                                                       [self.x + 47.5 + space, self.bumper],
                                                       [self.x + 200 + space, self.bumper]], 20)

    def drawT(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, self.bumper], 20)
        pygame.draw.line(surface, self.color, [self.x + 105 + space, self.bumper],
                         [self.x + 105 + space, surface.get_height() - self.bumper], 20)

    def drawU(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + space, surface.get_height() * .75],
                                                       [self.x + 47.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 157.5 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() * .75],
                                                       [self.x + 200 + space, self.bumper]], 20)

    def drawV(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 105 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, self.bumper]], 20)

    def drawW(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + 105 + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, self.bumper]], 20)

    def drawX(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + space, self.bumper],
                         [self.x + 200 + space, surface.get_height() - self.bumper],
                         20)
        pygame.draw.line(surface, self.color, [self.x + space, surface.get_height() - self.bumper],
                         [self.x + 200 + space, self.bumper],
                         20)

    def drawY(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 105 + space, surface.get_height() / 2],
                                                       [self.x + 200 + space, self.bumper]], 20)
        pygame.draw.line(surface, self.color, [self.x + 105 + space, surface.get_height() / 2],
                         [self.x + 105 + space, surface.get_height() - self.bumper], 20)

    def drawZ(self, surface, space):
        pygame.draw.lines(surface, self.color, False, [[self.x + space, self.bumper],
                                                       [self.x + 200 + space, self.bumper],
                                                       [self.x + space, surface.get_height() - self.bumper],
                                                       [self.x + 200 + space, surface.get_height() - self.bumper]], 20)

    def drawComma(self, surface, space):
        pygame.draw.line(surface, self.color, [self.x + 47.5 + space, surface.get_height() * .75],
                         [self.x + space, surface.get_height() - self.bumper], 20)

    def drawPeriod(self, surface, space):
        pygame.draw.circle(surface, self.color, (self.x + space, surface.get_height() - self.bumper - 10), 10)

    def update(self, surface, space):
        self.x -= 15
        if self.x <= -space:
            self.x = surface.get_width() + 10

def draw_all(surface, a: WriteLetter, letterList=None):
    if letterList is None:
        letterList = []
    space = 0
    surface.fill("White")
    for char in letterList:
        char = char.upper()
        if char == "A":
            WriteLetter.drawA(a, surface, space)
        elif char == "B":
            WriteLetter.drawB(a, surface, space)
        elif char == "C":
            WriteLetter.drawC(a, surface, space)
        elif char == "D":
            WriteLetter.drawD(a, surface, space)
        elif char == "E":
            WriteLetter.drawE(a, surface, space)
        elif char == "F":
            WriteLetter.drawF(a, surface, space)
        elif char == "G":
            WriteLetter.drawG(a, surface, space)
        elif char == "H":
            WriteLetter.drawH(a, surface, space)
        elif char == "I":
            WriteLetter.drawI(a, surface, space)
        elif char == "J":
            WriteLetter.drawJ(a, surface, space)
        elif char == "K":
            WriteLetter.drawK(a, surface, space)
        elif char == "L":
            WriteLetter.drawL(a, surface, space)
        elif char == "M":
            WriteLetter.drawM(a, surface, space)
        elif char == "N":
            WriteLetter.drawN(a, surface, space)
        elif char == "O":
            WriteLetter.drawO(a, surface, space)
        elif char == "P":
            WriteLetter.drawP(a, surface, space)
        elif char == "Q":
            WriteLetter.drawQ(a, surface, space)
        elif char == "R":
            WriteLetter.drawR(a, surface, space)
        elif char == "S":
            WriteLetter.drawS(a, surface, space)
        elif char == "T":
            WriteLetter.drawT(a, surface, space)
        elif char == "U":
            WriteLetter.drawU(a, surface, space)
        elif char == "V":
            WriteLetter.drawV(a, surface, space)
        elif char == "W":
            WriteLetter.drawW(a, surface, space)
        elif char == "X":
            WriteLetter.drawX(a, surface, space)
        elif char == "Y":
            WriteLetter.drawY(a, surface, space)
        elif char == "Z":
            WriteLetter.drawZ(a, surface, space)
        elif char == ",":
            WriteLetter.drawComma(a, surface, space)
            space -= 152.5
        elif char == ".":
            WriteLetter.drawPeriod(a, surface, space)
            space -= 152.5
        space += 250
    WriteLetter.update(a, surface, space)
    pygame.display.update()

def banner():
    running = True
    inputStr = input("Type what you want your banner to say ")
    inputList = list(inputStr)
    surface = pygame.display.set_mode((1450, 400))
    a = WriteLetter(surface)
    while running:
        draw_all(surface, a, inputList)
        pygame.time.wait(33)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False

banner()
