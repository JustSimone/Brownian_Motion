import pygame as pg
import numpy as np
from classes import molecule as ml

def bouncing_speed(body, molecule):
    # Velocities
    v1 = body.get_velocity()
    v1x = body.get_xvelocity()
    v1y = body.get_yvelocity()
    v2 = molecule.get_velocity()
    v2x = molecule.get_xvelocity()
    v2y = molecule.get_yvelocity()
    # Masses
    m1 = body.get_mass()
    m2 = molecule.get_mass()
    M = m1 + m2
    # Positions
    x1, y1 = body.shape.center
    x2, y2 = molecule.shape.center
    # DotProduct and Norms
    if(x1!=x2 and v1!=v2):
        dot1 = (v2x-v1x)*(x2-x1)+(v2y-v1y)*(y2-y1)
        dot2 = (v1x-v2x)*(x1-x2)+(v1y-v2y)*(y1-y2)
        norm = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
        new_v1x = v1x - 2*(m1/M)*((dot1)/norm)*(x1-x2)
        new_v1y = v1y - 2*(m1/M)*((dot1)/norm)*(y1-y2)
        new_v2x = v2x - 2*(m2/M)*((dot2)/norm)*(x2-x1)
        new_v2y = v2y - 2*(m2/M)*((dot2)/norm)*(y2-y1)
        new_v1 = [new_v1x, new_v1y]
        new_v2 = [new_v2x, new_v2y]
        body.set_velocity(new_v1)
        molecule.set_velocity(new_v2)
    else:
        body.set_velocity(v1)
        molecule.set_velocity(v2)
def bouncing(molecules, body, N):
    body_position = body.shape.center
    body_velocity = body.get_velocity()
    body_mass = body.get_mass()
    molecule_mass = molecules[0].get_mass()
    radius2 = body_mass*body_mass + molecule_mass*molecule_mass
    for molecule in molecules:
        molecule_position = molecule.shape.center
        molecule_velocity = molecule.get_velocity()
        distance2 = (molecule_position[0] - body_position[0])*(molecule_position[0] - body_position[0]) + (molecule_position[1] - body_position[1])*(molecule_position[1] - body_position[1])
        if distance2 <= 2*radius2:
            bouncing_speed(body, molecule)

def main():
    pg.init()
    screen = pg.display.set_mode([700, 700])
    running = True
    num_mol = 50
    mass_particles = 5
    mass_body = 50

    molecules = ml.Molecules(num_mol, screen, mass_particles)
    body = ml.Molecule(screen, 0, mass_body)
    body.set_velocity([0,0])

    print(screen.get_size())
    while running:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        vector_of_molecules = molecules.get_vector_of_molecules()
        bouncing(vector_of_molecules, body, num_mol)

        body.draw_a_particle(screen)
        molecules.draw_particles(screen)
        body.move_a_particle(screen)
        molecules.move_particles(screen)

        pg.time.delay(30)
        pg.display.update()


    pg.quit()

main()
