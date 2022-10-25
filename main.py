import pygame as pg
from classes import molecule as ml

pg.init()
screen = pg.display.set_mode([500, 500])
running = True
num_mol = 500
mass_particles = 2
mass_body = 15

molecules = ml.Molecules(num_mol, screen, mass_particles)
body = ml.Molecule(screen, 0, mass_body)

print(screen.get_size())
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    body.draw_a_particle(screen)
    molecules.draw_particles(screen)
    body.move_a_particle(screen)
    molecules.move_particles(screen)
    
    pg.time.delay(25)
    pg.display.update()


pg.quit()
