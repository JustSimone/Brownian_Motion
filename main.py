import pygame as pg
from classes import molecule

pg.init()
screen = pg.display.set_mode([500, 500])
running = True
num_mol = 100

molecules = molecule.Molecules(num_mol, screen)

print(screen.get_size())
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    molecules.draw_particles(screen)
    molecules.move_particles()
    molecules.bounce_off_the_wall(screen)
    pg.time.delay(50)
    pg.display.update()

pg.quit()
