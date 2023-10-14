import pygame

def win_check(symbol):
    if field[0][0] == field[0][1] == field[0][2] == symbol: 
        print(symbol,"has won!")
        return False #elif for all the other posibilities (77 other lines)
    elif field[1][0] == field[1][1] == field[1][2] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[2][0] == field[2][1] == field[2][2] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[0][0] == field[1][0] == field[2][0] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[0][1] == field[1][1] == field[2][1] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[0][2] == field[1][2] == field[2][2] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[0][0] == field[1][1] == field[2][2] == symbol: 
        print(symbol,"has won!")
        return False
    elif field[2][0] == field[1][1] == field[0][2] == symbol: 
        print(symbol,"has won!")
        return False
    else:
        return True


wdth = 300
hgth = 300

red = (255, 0, 0)
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (173, 216, 230)
sage = "#B2AC88"

turns = 0

field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

run = True

pygame.init()
screen = pygame.display.set_mode((wdth , hgth))
pygame.display.set_caption("GAME")
screen.fill(light_blue)
pygame.draw.line(screen , black, (100,0),(100, 300), 5) 
pygame.draw.line(screen , black, (200,0),(200, 300), 5)
pygame.draw.line(screen , black, (0,100),(300, 100), 5)
pygame.draw.line(screen , black, (0,200),(300, 200), 5)
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if field[pos[1]//100][pos[0]//100] == '':
                turns += 1
                if  turns%2 == 1:    
                    field[pos[1]//100][pos[0]//100] = 'x'
                    pygame.draw.line(screen,blue, (0 + 100 * (pos[0] // 100),0 + 100 * (pos[1] // 100)), (100 + 100 * (pos[0] // 100), 100 + 100 * (pos[1] // 100)) , 7 ) #do it for every line
                    pygame.draw.line(screen,blue, (100 + 100 * (pos[0] // 100),0 + 100 * (pos[1] // 100)), (0 + 100 * (pos[0] // 100), 100 + 100 * (pos[1] // 100)) , 7 )
                    pygame.display.flip()
                    print(field)
                    run = win_check('x')
                else:
                    field[pos[1]//100][pos[0]//100] = 'o'
                    pygame.draw.circle(screen, blue, (50 + 100 * (pos[0] // 100),50 + 100 * (pos[1] // 100)), (50), (7))
                    pygame.display.flip()
                    print(field)
                    run = win_check('o')
                
pygame.quit()

