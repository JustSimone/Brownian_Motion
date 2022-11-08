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
    # Dot product
    dot1 = (v1x - v2x)*(x1 - x2) + (v1y - v2y)*(y1 - y2)
    dot2 = (v2x - v1x)*(x2 - x1) + (v2y - v1y)*(y2 - y1)
    # Norm
    norm = (x2 - x1)*(x2 -x1) + (y2 - y1)*(y2 - y1)

    new_vx1 = v1x - (2*m1/M)*(dot1/norm)*(x1-x2)
    new_vy1 = v1y - (2*m1/M)*(dot1/norm)*(y1-y2)
    new_vx2 = v2x - (2*m2/M)*(dot2/norm)*(x2-x1)
    new_vy2 = v2y - (2*m2/M)*(dot2/norm)*(y2-y1)

    new_v1 = [new_vx1, new_vy1]
    new_v2 = [new_vx2, new_vy2]

    body.set_velocity(new_v1)
    molecule.set_velocity(new_v2)
def bouncing(molecules, body, N):
    body_position = body.shape.center
    body_velocity = body.get_velocity()
    body_mass = body.get_mass()
    molecule_mass = molecules[0].get_mass()
    radius2 = body_mass*body_mass + molecule_mass*molecule_mass
    for i in range(N):
        molecule_position = molecules[i].shape.center
        molecule_velocity = molecules[i].get_velocity()
        distance2 = (molecule_position[0] - body_position[0])*(molecule_position[0] - body_position[0]) + (molecule_position[1] - body_position[1])*(molecule_position[1] - body_position[1])
        if (distance2 <= 1.*radius2):
            #bouncing_speed(body, molecules[i])
            body.set_velocity([-body.get_xvelocity(),-body.get_yvelocity()])
            molecules[i].set_velocity([-molecules[i].get_xvelocity(),-molecules[i].get_yvelocity()])
            print(molecules[i].get_id())
def main():
    pg.init()
    screen = pg.display.set_mode([700, 700])
    running = True
    num_mol = 100
    mass_particles = 1
    mass_body = 40

    body = ml.Molecule(screen, 0, mass_body)
    molecules = ml.Molecules(num_mol, screen, mass_particles, mass_body, body.get_position())
    body.set_velocity([1,1])

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
