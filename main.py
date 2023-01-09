#Name: Swayem
#Start Date: December 7, 2022
#Program Name: The Surface
#Purpose: Opposite to the ASCII art game "The Cave", it will be a zelda type of game with abilities, save system, 

import pygame, sys
from pygame.locals import QUIT
from button import Button

#Initializes the screen and sets dimensions
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))

#Defines the background image for the menu
BG = pygame.image.load("assets/Menu_image.png")

#Gets the font from the assets file and labeles the size
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def play_select():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_NEW = Button(image=None, pos=(640, 180), text_input="New Game", font=get_font(75), base_color='White', hovering_color="Green")
        PLAY_NEW.changeColor(PLAY_MOUSE_POS)
        PLAY_NEW.update(SCREEN)
          
        PLAY_LOAD = Button(image=None, pos=(640, 320), text_input="Load Game", font=get_font(75), base_color='White', hovering_color="Green")
        PLAY_LOAD.changeColor(PLAY_MOUSE_POS)
        PLAY_LOAD.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                    new_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_LOAD.checkForInput(PLAY_MOUSE_POS):
                    main_menu()            


        pygame.display.update()


def new_game():
    while True:

      NEW_MOUSE_POS = pygame.mouse.get_pos()
      SCREEN.fill("white")
      PLAY_NEW = Button(image=None, pos=(640, 180), text_input="hehehe", font=get_font(75), base_color='White', hovering_color="Green")
      PLAY_NEW.changeColor(NEW_MOUSE_POS)
      PLAY_NEW.update(SCREEN)

      pygame.display.update()

def options():
    while True:
        #Gets the moise position for button collisions
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #Fills the screen with white and overlaps the previous screen
        SCREEN.fill("white")

        #Puts in the text for the options placeholder for future changes, makes rectangle and places it in the same position
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("The Surface", True, "#00F3FF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_select()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()