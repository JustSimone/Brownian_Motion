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
        x = rnd.randrange(1 + mass, x_size - mass)
        y = rnd.randrange(1 + mass, y_size - mass)

        self.mass_partice = mass
        # Generator of the velocity of the particles, all with different direction,
        # but with the same module.
        theta = rnd.uniform(0, 2*np.pi)
        vx = np.cos(theta)
        vy = np.sin(theta)

        self.velocity = [vx, vy]

        self.shape = pg.rect.Rect(x,y, self.mass_partice, self.mass_partice)
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

    # Setter Methods
    def set_velocity(self, new_v):
        self.velocity = new_v
        #print(self.velocity)
    def set_xvelocity(self, new_vx):
        self.velocity[0] = new_vx
    def set_yvelocity(self, new_vy):
        self.velocity[1] = new_vy

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
    def __init__(self, N, fScreen, mass):
        self.number_of_molecules = N
        self.mass = mass
        self.molecules = []
        for i in range(self.number_of_molecules):
            molecule = Molecule(fScreen, i, self.mass)
            self.molecules.append(molecule)

    #Molecules Functions

    def get_vector_of_molecules(self):
        return self.molecules
    def draw_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            pg.draw.circle(fScreen, (255, 255, 255), self.molecules[i].shape.center, self.mass)
    def move_particles(self, fScreen):
        # mass_1 = self.mass
        # mass_2 = mass_1
        # radius2 = self.mass * self.mass
        # N = self.number_of_molecules

        for i in range(self.number_of_molecules):
            v = self.molecules[i].get_velocity()
            self.molecules[i].shape = self.molecules[i].shape.move(10*v[0], 10*v[1])

            x_size, y_size = fScreen.get_size()

            x = self.molecules[i].shape.x
            y = self.molecules[i].shape.y

            #Bouncing off the wall
            if x<0+self.mass or x>x_size-self.mass:
                self.molecules[i].set_xvelocity(-self.molecules[i].get_xvelocity())
            if y<0+self.mass or y>y_size-self.mass:
                self.molecules[i].set_yvelocity(-self.molecules[i].get_yvelocity())

            #Bouncing against each other

            # molecule_position = self.molecules[i].shape.center
            # molecule_velocity = self.molecules[i].get_velocity()
            # for j in range(N):
            #     if i != j:
            #         other_molecule_position = self.molecules[j].shape.center
            #         other_molecule_velocity = self.molecules[j].get_velocity()
            #         distance2 = (molecule_position[0] - other_molecule_position[0])*(molecule_position[0] - other_molecule_position[0]) + (molecule_position[1] - other_molecule_position[1])*(molecule_position[1] - other_molecule_position[1])
            #         if distance2 < 4*radius2:
            #
            #             self.molecules[i].set_velocity([-self.molecules[i].get_xvelocity(), -self.molecules[i].get_yvelocity()])
            #             self.molecules[j].set_velocity([-self.molecules[j].get_xvelocity(), -self.molecules[j].get_yvelocity()])
