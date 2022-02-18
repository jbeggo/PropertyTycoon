import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((910, 910), pygame.RESIZABLE)
pygame.display.set_caption("Property Tycoon")
clock = pygame.time.Clock()
WIDTH = HEIGHT = 910

# create board sections

centre = pygame.Surface((630, 630))
centre.fill('White')

# draw text
titleFont = pygame.font.Font('fonts/monoton.ttf', 50)
titleText = titleFont.render('Property Tycoon', True, 'Black')
titleTextRect = titleText.get_rect(center=(455, 455))

# CORNERS
freeParking = pygame.Surface((140, 140))
freeParking.fill('White')
go = pygame.Surface((140, 140))
go.fill('White')
goToJail = pygame.Surface((140, 140))
goToJail.fill('White')
jail = pygame.image.load('graphics/jail.png')

# PLACES

# Oranges
broyles = pygame.Surface((140, 70))
dunham = pygame.Surface((140, 70))
bishop = pygame.Surface((140, 70))
broyles.fill('Orange')
dunham.fill('Orange')
bishop.fill('Orange')
# Purples
rey = pygame.image.load('graphics/rey.png')
wookie = pygame.image.load('graphics/wookie.png')
skywalker = pygame.image.load('graphics/skywalker.png')
#rey.fill('Purple')
#wookie.fill('Purple')
#skywalker.fill('Purple')
# Reds
hanxin = pygame.Surface((70, 140))
mulan = pygame.Surface((70, 140))
yuefei = pygame.Surface((70, 140))
hanxin.fill('Red')
mulan.fill('Red')
yuefei.fill('Red')
# Yellows
crusher = pygame.Surface((70, 140))
picard = pygame.Surface((70, 140))
shatner = pygame.Surface((70, 140))
crusher.fill('Yellow')
picard.fill('Yellow')
shatner.fill('Yellow')
# Greens
ibis = pygame.Surface((140, 70))
ghengis = pygame.Surface((140, 70))
sirat = pygame.Surface((140, 70))
ibis.fill('Green')
ghengis.fill('Green')
sirat.fill('Green')
# Dark Blues
turing = pygame.Surface((140, 70))
james = pygame.Surface((140, 70))
turing.fill((43, 54, 255))
james.fill((43, 54, 255))
# Browns
gangsters = pygame.Surface((70, 140))
creek = pygame.Surface((70, 140))
gangsters.fill((210, 146, 106))
creek.fill((210, 146, 106))
# Light Blues
granger = pygame.Surface((70, 140))
potter = pygame.Surface((70, 140))
angel = pygame.Surface((70, 140))
granger.fill((43, 199, 255))
potter.fill((43, 199, 255))
angel.fill((43, 199, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # place corners
    screen.blit(freeParking, (0, 0))
    screen.blit(go, (770, 770))
    screen.blit(goToJail, (770, 0))
    screen.blit(jail, (0, 770))
    screen.blit(centre, (140, 140))

    # place title text
    screen.blit(titleText, titleTextRect)

    # place location pieces
    # place reds
    screen.blit(yuefei, (140, 0))
    screen.blit(mulan, (280, 0))
    screen.blit(hanxin, (350, 0))
    # place yellows
    screen.blit(shatner, (490, 0))
    screen.blit(picard, (560, 0))
    screen.blit(crusher, (700, 0))
    # place greens
    screen.blit(sirat, (770, 140))
    screen.blit(ghengis, (770, 210))
    screen.blit(ibis, (770, 350))
    # place dark blues
    screen.blit(james, (770, 490))
    screen.blit(turing, (770, 630))
    # place light blues
    screen.blit(granger, (140, 770))
    screen.blit(potter, (210, 770))
    screen.blit(angel, (350, 770))
    # place browns
    screen.blit(gangsters, (560, 770))
    screen.blit(creek, (700, 770))
    # place oranges
    screen.blit(broyles, (0, 140))
    screen.blit(dunham, (0, 210))
    screen.blit(bishop, (0, 350))
    # place purples
    screen.blit(rey, (0, 490))
    screen.blit(wookie, (0, 560))
    screen.blit(skywalker, (0, 700))

    # draw & update
    pygame.display.update()
    clock.tick(60)
