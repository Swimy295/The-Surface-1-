import pygame, sys, time
from pygame.locals import QUIT
from button import Button
from pygame import Color, Surface






intro = 0

#Initializes the screen and sets dimensions
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))

#Defines the background image for the menu
BG = pygame.image.load("assets/Menu_image.png")

#Gets the font from the assets file and labeles the size
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)



#Defines the main menu screen allowing the use of the options, play, and quit button. 
def main_menu():
    while True:

        #Places the background onto the screen and menu_mouse_pos gets the mouse position for button collision
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #Establishes the game title as the surface and then blits it onto the screen using the rectangle
        MENU_TEXT = get_font(100).render("The Surface", True, "#00F3FF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        #Establishes the play, options, and quit button using the button class in another file. This takes the positions, colour, font, text, and the image rectangle behind the button. Also establishes the normal colour as white, and the hovering clour as white.
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        
        #Checks for the the mouse position and then changes the button to the hovering colour
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        #Checks the event actions such as the close button on he top right, and then checks if the user presses the button and then switches to the different screen.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_select()
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                    break
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()





#Options screen that shows the controls of the game
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
                    break
              
        pygame.display.update()



#Play select screen. Determines if the user wants to load a save or start a new save.
def play_select():
    while True:

        #Blits background and checks for mouse position
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #Makes the New game button, load game button, and back to main menu button and then checks for mouse hovering and then updates depending on the hovering using the button class in button.py
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

        #Checks for the events that the user makes such as clicking on the new game, back, or load game button and switches to a different screen.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                    
                    new_game()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_LOAD.checkForInput(PLAY_MOUSE_POS):
                    
                    main_menu()            
                    break
        pygame.display.update()




#Gets the input for the user's name using the console. Works best with different tabs.
def new_game():
    while True:
        global NAME
        
        #gets mouse position in this screen and fills the screen with white.
        NEW_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        #Places text on the screen using the rectangle created for the position and blits it to the screen to tell the user to look at the console
        Console_text = get_font(50).render("Please look at console", True, "#00F3FF")
        Console_rect = Console_text.get_rect(center=(640, 200))
        SCREEN.blit(Console_text, Console_rect)

        #Back button from the previous functions using the button class
        SELECT_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")
        SELECT_BACK.changeColor(NEW_MOUSE_POS)
        SELECT_BACK.update(SCREEN)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
                  
        #Gets the input from the console and assigns it into the next function
        pygame.display.update()

        #Checks for the name input and if it numbers or blank it asks for it again, and if it is, sends the user to the intro sequence
        while True:
          NAME = input("What is your name, risen?: ")
          if NAME.isdigit():
            print(" ")
          else:
            print("Please look back at the output")
            break
        break
    intro_newsave()



#Intro/new save where it plays a short intro sequence and also saves the name into a new file
def intro_newsave():
  while True:
    global NAME

    #The saves list that encases the information to put into the file
    saves = [
    NAME
    ]

    #Opens the file if there, or makes a new file and puts it into the write mode. Takes all of the lines in the saves list and writes it into the file in different lines and closes the file.
    f = open("load.txt", "w")
    for item in saves:
      f.write(item + "\n")
    f.close()
    
    SCREEN.fill("White")

    #First text that makes the intro more dramatic and loads it seperately and blits it onto the screen
    one_text = get_font(30).render("I see you have got out of the cave", True, "#00F3FF")
    SCREEN.blit(one_text, (140, 150))
    pygame.display.update()

    #Pauses the code for 5 seconds
    time.sleep(5)

    #Plays the next line on the screen with the characters name on the screen
    second_text = get_font(30).render("There are many things to do, " + NAME , True, "#00F3FF")
    SCREEN.blit(second_text, (140, 300))
    pygame.display.update()

    #Pauses the code for 5 seconds
    time.sleep(5)

    #Plays the 3rd text and then blits it to the screen
    third_text = get_font(30).render("Many things have changed since the cave", True, "#00F3FF")
    SCREEN.blit(third_text, (100, 450))
    pygame.display.update()

    time.sleep(7)

    #Loads the intro image and then the logo on the on image
    intro = pygame.image.load("assets/intro_image.png")
    THE_SURFACE_LOGO = pygame.image.load("assets/Surface_image.png")
    
    SCREEN.blit(intro, (0,0))
    SCREEN.blit(THE_SURFACE_LOGO, (300, 300))
    pygame.display.update()

    #pause for 7 seconds
    time.sleep(7)
    break
  end_intro()

def end_intro():
  while True:
    global intro
    intro += 1
    SCREEN.fill("White")
    pygame.display.update()
    
