import numpy as np
import pygame as pg
import random as rnd

# Generator of the velocity of the particles, all with different direction,
# but with the same module, in this case 1 +/- 0.001.
def speed_generator():
    vx = 0
    vy = 0
    c = 0

    while (c < 0.999) or (c > 1.001):
        x = rnd.uniform(-1., 1)
        y = rnd.uniform(-1., 1)
        c = np.sqrt(x*x+y*y)
    return [x,y]

# Molecule class, defining what a molecule object is giving it a momentum and a initial position
class Molecule:
    def __init__(self, fScreen, fIndex):
        x_size, y_size = fScreen.get_size()
        x = rnd.randrange(1, x_size)
        y = rnd.randrange(1, y_size)

        velocity = speed_generator()
        self.velocity = velocity
        self.v_x = velocity[0]
        self.v_y = velocity[1]

        self.shape = pg.rect.Rect(x,y, 2,2)
        self.index = fIndex

    # Getter Methods
    def get_velocity(self):
        return self.velocity

    def get_xvelocity(self):
        return self.v_x

    def get_yvelocity(self):
        return self.v_y

    # Setter Methods
    def set_xvelocity(self, new_vx):
        self.v_x = new_vx

    def set_yvelocity(self, new_vy):
        self.v_y = new_vy

# Molecules class, defining a set of molecules interacting and moving together
class Molecules:
    def __init__(self, N, fScreen):
        self.number_of_molecules = N
        self.mass = 1
        self.molecules = []
        for i in range(self.number_of_molecules):
            molecule = Molecule(fScreen, i)
            self.molecules.append(molecule)

    def draw_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            pg.draw.circle(fScreen, (255, 255, 255), self.molecules[i].shape.center, self.mass)

    def move_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            v = self.molecules[i].get_velocity()
            self.molecules[i].shape = pg.Rect.move(self.molecules[i].shape, 1.5*v[0], 1.5*v[1])

            x_size, y_size = fScreen.get_size()

            x = self.molecules[i].shape.x
            y = self.molecules[i].shape.y

            if x<10 or x>50:
                self.molecules[i].set_xvelocity(-self.molecules[i].get_xvelocity())
            if y<10 or y>50:
                self.molecules[i].set_yvelocity(-self.molecules[i].get_yvelocity())
