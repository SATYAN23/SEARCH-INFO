import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import sys
import pandas as pd
import numpy as np
import os
#import warnings
import pyautogui
width, height = pyautogui.size()

#warnings.filterwarnings("ignore")


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((73.15*width)/100, (46.6*height)/100)
    
i_icon = os.getcwd() + ".\R.ico"
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INFO")
font = pygame.font.SysFont("Segoe UI ", 16)

theme = os.getcwd() + ".\entry_line.json"
manager = pygame_gui.UIManager((500, 500), theme)
manager.get_theme().load_theme(theme)
text_input1 = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((250, 300), (200, 30)),
     manager = manager, object_id = ObjectID(class_id = "text_entry_line",
                                             object_id = '#main_text_entry1'))
text_input2 = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((250, 350), (200, 30)),
     manager = manager, object_id = ObjectID(class_id = "text_entry_line",
                                             object_id = '#main_text_entry2'))

text_input3 = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((250, 100), (200, 30)),
     manager = manager, object_id = ObjectID(class_id = "text_entry_line",
                                             object_id = '#main_text_entry3'))


clock = pygame.time.Clock()
data = pd.read_csv(".\data_info.csv")
li = data["Name"].tolist()
li1 = data["Phonenumber"].tolist()
text1 = ''
text2 = ''
li = li
li1 = li1
number = ''

dataset = pd.read_csv(".\data_info.csv")

class main():

    def username():
        global X, Y, li, li1, number
        
        while True:

            UI_REFRESH_RATE = clock.tick(60) / 1000
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                     event.ui_object_id == '#main_text_entry1'):
                    text1 = str(event.text)
                    li.append(text1)
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                     event.ui_object_id == '#main_text_entry2'):
                    text2 = int(event.text)   
                    li1.append(text2)
                    df = pd.DataFrame()
                    df["Name"] = li
                    df["Phonenumber"] = li1
                    df.to_csv(".\data_info.csv", index = False)

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry3'):
                    text1 = str(event.text)

                    if text1 in li:
                        n = li.index(text1)
                        number = str(text1) + " : " + str(li1[n])
                    else:
                        number =  str("NAME NOT FOUND")

                manager.process_events(event)
        
            manager.update(UI_REFRESH_RATE)
        
            SCREEN.fill((211, 211, 211))
            textname = font.render("Enter_Name", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 300))
            textname = font.render("Enter_Number", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 350))
            textname = font.render("Search_Name", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 100))
            textname = font.render(number, True, (96, 96, 96))
            SCREEN.blit(textname, (250, 150))
            manager.draw_ui(SCREEN)
            pygame.display.update()
        
    username()

if name == "main":
    main()
