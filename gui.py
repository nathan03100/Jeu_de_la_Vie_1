

import threading

import pygame
import pygame.gfxdraw
from PyQt5.QtWidgets import QWidget
import time
from damier import Damier
from simulation import Simulation

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
t = 0


class Gui(threading.Thread, QWidget):
    def __init__(self):
        threading.Thread.__init__(self)
        super().__init__()
        # tailles de cases
        self.width = 20
        self.height = 20
        # espace entre les cases
        self.margin = 5
        # les tableaux
        self.grid = []
        self.case = []
        self.case1 = []
        n = -1
        p = -1
        self.b=0
        self.c=0
        self.test=0
        self.a=0
        nbr_generation = 0


        self.nbx = Damier.longueur(n)
        self.nby = Damier.largeur(p)
        self.nbr_generation = Simulation.nbr_génération(nbr_generation)

        for row in range(self.nbx):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.nby):
                self.grid[row].append(0)  # Append a cell

    def updateCell(self, x, y, valeur):
        self.grid[x - 1][y - 1] = valeur

    i = 0

    def cellulenaissante(self):
            for j in range(0, len(self.grid)):
                for i in range(0, len(self.grid[0])):
                    if self.grid[j][i] == 1 and not i <= 0 and not j <= 0 and not i >= self.nbx - 1 and not j >= self.nby - 1 and self.a < self.nbr_generation-1:
                        self.test=1
                        self.case.append(j + 1)
                        self.case1.append(i)
                        self.case.append(j - 1)
                        self.case1.append(i)
                        self.case.append(j)
                        self.case1.append(i + 1)
                        self.case.append(j)
                        self.case1.append(i - 1)
                        with open('save_self_case.txt', 'w') as f:
                            for item in self.case:
                                f.write(f'{item}\n')

                        with open('save_self_case1.txt', 'w') as t:
                            for item in self.case1:
                                t.write(f'{item}\n')




                # cas particulier colone 0 et ligne zéro

    def colornewcell(self):
        nb = 0
        nb = len(self.case)
        n = 0
        if self.a < self.nbr_generation-1:
            while n != nb :
                  r = self.case[0]
                  u = self.case1[0]
                  self.grid[r][u] = 1
                  del self.case[0]
                  del self.case1[0]
                  n = n + 1


    def cellulemorte(self):

        for j in range(0, len(self.grid)):
            for i in range(0, len(self.grid[0])):
                if self.grid[j][i] == 1 and not i <= 0 and not j <= 0 and not i >= self.nbx - 1 and not j >= self.nby - 1 and self.a < self.nbr_generation-1:
                    if self.grid[j + 1][i] == 1:
                        if self.grid[j - 1][i] == 1:

                            if self.grid[j][i - 1] == 1:

                                if self.grid[j][i + 1] == 1:

                                    self.grid[j][i] = 0



    def run(self, n=-1, p=-1, x="", flag=1, g=-1, w=-1, y=-1, j=-1, o=-1,nbr_generation=-1):
        # Initialize pygame
        pygame.init()
        WINDOW_SIZE = [self.nbx * (self.width + self.margin), self.nby * (self.height + self.margin)]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(Damier.nom(x))

        # Loop until the user clicks the close button.
        done = False

        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            screen.fill(BLACK)

            # Draw the grid

            for row in range(self.nbx):
                for column in range(self.nby):
                    color = WHITE
                    if self.grid[row][column] == 1:
                        color = GREEN
                    if self.grid[row][column] == 2:
                        color = RED
                    if self.grid[row][column] == 3:
                        color = BLACK
                    if self.grid[row][column] == 0:
                        color = WHITE
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])

            if self.c == 0:
                self.b = int(input("recupérer la sauvegarde précédente (oui:1/non:0)"))
                if self.b == 1:
                    with open('save_self_case.txt', 'r')as f:
                        self.case = f.read().splitlines()
                        self.case = list(map(int, self.case))
                    with open('save_self_case1.txt', 'r')as d:
                        self.case1 = d.read().splitlines()
                        self.case1 = list(map(int, self.case1))

                        self.c = self.c + 1
                else:
                     self.c = self.c + 1


            self.cellulenaissante()
            self.colornewcell()
            self.cellulemorte()
            if self.test == 1:
                self.a = self.a + 1



            time.sleep(1)
            # Limit to 60 frames per second
            clock.tick(1)

            test = 0
            # Go ahead and update the screen with what we've drawn.

            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'

        # on exit.
        pygame.quit()
