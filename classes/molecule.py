import numpy as np
import pygame as pg
from pygame import math
import numpy as np
import random as rnd

# Generator of the velocity of the particles, all with different direction,
# but with the same module, in this case 1.

def bouncing_speed(m1, m2, v1, v2, r1, r2):
    #Defining the positions used in the equations
    x1 = r1[0]
    y1 = r1[1]
    x2 = r2[0]
    y2 = r2[1]
    #Desining the velocities used in the equations
    vx1 = v1[0]
    vy1 = v1[1]
    vx2 = v2[0]
    vy2 = v2[1]
    #Total mass of the system
    M = m1 + m2
    #Dot product of the differences of the velocity and the positions
    dot_product1 = (vx1 - vx2)*(x1 - x2) + (vy1 - vy2)*(y1 - y2)
    dot_product2 = (vx2 - vx1)*(x2 - x1) + (vy2 - vy1)*(y2 - y1)
    #Norm of the position vector
    norm_position1 = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
    norm_position2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
    #Computing the new velocities based on the collision
    new_vx1 = vx1 - 2*(m1/M)*(dot_product1/norm_position1)* (x1-x2)
    new_vy1 = vy1 - 2*(m1/M)*(dot_product1/norm_position1)* (y1-y2)
    new_vx2 = vx2 - 2*(m2/M)*(dot_product2/norm_position2)* (x2-x1)
    new_vy2 = vy2 - 2*(m2/M)*(dot_product2/norm_position2)* (y2-y1)
    #Putting toghter the new velocity vector
    new_v1 = [new_vx1, new_vy1]
    new_v2 = [new_vx2, new_vy2]
    return [new_v1, new_v2]

# Molecule class, defining what a molecule object is giving it a momentum and a initial position
class Molecule:
    def __init__(self, fScreen, fIndex, mass):
        x_size, y_size = fScreen.get_size()
        x = rnd.randrange(1 + mass, x_size - mass)
        y = rnd.randrange(1 + mass, y_size - mass)

        self.theta = 1*np.pi*rnd.random()
        vx = np.sin(self.theta)
        vy = np.cos(self.theta)

        self.velocity = [vx, vy]

        self.shape = pg.rect.Rect(x,y, 2,2)
        self.index = fIndex

    # Getter Methods
    def get_velocity(self):
        return self.velocity
    def get_xvelocity(self):
        return self.velocity[0]
    def get_yvelocity(self):
        return self.velocity[1]

    # Setter Methods
    def set_velocity(self, new_v):
        self.velocity = new_v
        #print(self.velocity)
    def set_xvelocity(self, new_vx):
        self.velocity[0] = new_vx
    def set_yvelocity(self, new_vy):
        self.velocity[1] = new_vy

# Molecules class, defining a set of molecules interacting and moving together
class Molecules:
    def __init__(self, N, fScreen, mass):
        self.number_of_molecules = N
        self.mass = mass
        self.molecules = []
        for i in range(self.number_of_molecules):
            molecule = Molecule(fScreen, i, self.mass)
            self.molecules.append(molecule)

    #Molecules Functions

    def draw_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            pg.draw.circle(fScreen, (255, 255, 255), self.molecules[i].shape.center, self.mass)
    def move_particles(self, fScreen):
        for i in range(self.number_of_molecules):
            v = self.molecules[i].get_velocity()
            self.molecules[i].shape = self.molecules[i].shape.move(1.5*v[0], 1.5*v[1])

            x_size, y_size = fScreen.get_size()

            x = self.molecules[i].shape.x
            y = self.molecules[i].shape.y
            #Bouncing off the wall
            if x<0+self.mass or x>x_size-self.mass:
                self.molecules[i].set_xvelocity(-self.molecules[i].get_xvelocity())
            if y<0+self.mass or y>y_size-self.mass:
                self.molecules[i].set_yvelocity(-self.molecules[i].get_yvelocity())

            #Particle collisions
            mass_1 = self.mass
            mass_2 = mass_1
            radius2 = self.mass * self.mass
            N = self.number_of_molecules
            for i in range(N):
                molecule_position = self.molecules[i].shape.center
                molecule_velocity = self.molecules[i].get_velocity()
                for j in range(N):
                    if i != j:
                        other_molecule_position = self.molecules[j].shape.center
                        other_molecule_velocity = self.molecules[j].get_velocity()
                        distance2 = (molecule_position[0] - other_molecule_position[0])*(molecule_position[0] - other_molecule_position[0]) + (molecule_position[1] - other_molecule_position[1])*(molecule_position[1] - other_molecule_position[1])
                        if distance2 < 4*radius2:
                            new_velocity = bouncing_speed(mass_1, mass_2, molecule_velocity, other_molecule_velocity, molecule_position, other_molecule_position)
                            self.molecules[i].set_velocity(new_velocity[0])
                            self.molecules[j].set_velocity(new_velocity[1])
                            break
