import numpy as np
import pygame as pg
from pygame import math
import numpy as np
import random as rnd

# Molecule class, defining what a molecule object is giving it a momentum and a initial position
class Molecule:
    # Class variables theta, velocity, shape, index
    def __init__(self, fScreen, fIndex, mass):
        x_size, y_size = fScreen.get_size()
        self.x = rnd.randrange(1 + mass, x_size - mass)
        self.y = rnd.randrange(1 + mass, y_size - mass)

        self.mass_partice = mass
        # Generator of the velocity of the particles, all with different direction,
        # but with the same module.
        theta = rnd.uniform(0, 2*np.pi)
        vx = np.cos(theta)
        vy = np.sin(theta)

        self.velocity = [vx, vy]

        self.shape = pg.rect.Rect(self.x,self.y, self.mass_partice, self.mass_partice)
        self.index = fIndex

    # Getter Methods
    def get_velocity(self):
        return self.velocity
    def get_xvelocity(self):
        return self.velocity[0]
    def get_yvelocity(self):
        return self.velocity[1]
    def get_mass(self):
        return self.mass_partice
    def get_id(self):
        return self.index
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_position(self):
        return [self.x,self.y]

    # Setter Methods
    def set_velocity(self, new_v):
        self.velocity = new_v
        #print(self.velocity)
    def set_xvelocity(self, new_vx):
        self.velocity[0] = new_vx
    def set_yvelocity(self, new_vy):
        self.velocity[1] = new_vy
    def set_id(self, new_id):
        self.index = new_id

    #Draw a Particle
    def draw_a_particle(self, fScreen):
        pg.draw.circle(fScreen, (255, 255, 255), self.shape.center, self.mass_partice)
    def move_a_particle(self, fScreen):
        v = self.velocity
        self.shape = self.shape.move(1.5*v[0], 1.5*v[1])

        x_size, y_size = fScreen.get_size()

        x = self.shape.x
        y = self.shape.y
        #Bouncing off the wall
        if x<0+self.mass_partice or x>x_size-self.mass_partice:
            self.velocity[0] = -self.velocity[0]
        if y<0+self.mass_partice or y>y_size-self.mass_partice:
            self.velocity[1] = -self.velocity[1]

class Molecules:
    # Class variables number_of_molecules, mass, molecules
    def __init__(self, N, fScreen, mass, mass_body, body_position):
        self.number_of_molecules = N
        self.mass = mass
        self.molecules = []
        i = 0
        while i<N:
            new_molecule = Molecule(fScreen, i, self.mass)
            if new_molecule.get_x() < body_position[0]-mass_body or new_molecule.get_x() > body_position[0]+mass_body:
                if new_molecule.get_y() < body_position[1]-mass_body or new_molecule.get_y() > body_position[1]+mass_body:
                    self.molecules.append(new_molecule)
                    i += 1
                    print(i)

    #Molecules Functions

    def get_vector_of_molecules(self):
        return self.molecules
    def draw_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            pg.draw.circle(fScreen, (255, 255, 255), self.molecules[i].shape.center, self.mass)
    def move_particles(self, fScreen):

        for i in range(self.number_of_molecules):
            v = self.molecules[i].get_velocity()
            self.molecules[i].shape = self.molecules[i].shape.move(5*v[0], 5*v[1])

            x_size, y_size = fScreen.get_size()

            x = self.molecules[i].shape.x
            y = self.molecules[i].shape.y

            #Bouncing off the wall
            if x<0+self.mass or x>x_size-self.mass:
                self.molecules[i].set_xvelocity(-self.molecules[i].get_xvelocity())
            if y<0+self.mass or y>y_size-self.mass:
                self.molecules[i].set_yvelocity(-self.molecules[i].get_yvelocity())
