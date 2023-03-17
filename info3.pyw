import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import sys
import pandas as pd
import os
import warnings
import pyautogui

import pygame_gui
import pygame_gui.data
from pygame.color import Color
from pygame.surface import Surface
from pygame_gui.elements.ui_text_box import UITextBox

width, height = pyautogui.size()
#warnings.filterwarnings("ignore")


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((10*width)/100, (10*height)/100)
    
i_icon = os.getcwd() + ".\R.ico"
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
WIDTH, HEIGHT = 700, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INFO")
font = pygame.font.SysFont("Segoe UI", 25)

theme = os.getcwd() + ".\entry_line.json"
theme1 = "text_box.json"
manager = pygame_gui.UIManager((700, 800), theme)
manager.get_theme().load_theme(theme)
manager.get_theme().load_theme(theme1)

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

cursor_toggle = 0


clock = pygame.time.Clock()
data = pd.read_csv(".\data_info.csv")
li = data["Name"].tolist()
li1 = data["Phonenumber"].tolist()
text1 = ''
text2 = ''
li = li
li1 = li1
arli = []
number = ''

class main():

    def username():
        global X, Y, li, li1, arli, number, cursor_toggle
        number = str("enter name") 
        
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

                text_box = UITextBox(
                           html_text=f"Hello,{number}""<body><font color=#000000>{number} "
                                  "hello you can be able to be a software engineer "
                                   "brand new friend? "
                                         "days of our" + str({number}) ,
                                   relative_rect=pygame.Rect((100, 500), (300, 100)),
                                          manager=manager, object_id = ObjectID(class_id = "text_box"))        
                        
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    text_block_full_height = text_box.text_box_layout.layout_rect.height
                    height_adjustment = (text_box.scroll_bar.start_percentage *
                                     text_block_full_height)
                    base_x = int(text_box.rect[0] + text_box.padding[0] + text_box.border_width +
                             text_box.shadow_width + text_box.rounded_corner_offset)
                    base_y = int(text_box.rect[1] + text_box.padding[1] + text_box.border_width +
                             text_box.shadow_width + text_box.rounded_corner_offset - height_adjustment)
                    text_box.text_box_layout.set_cursor_from_click_pos((event.pos[0] - base_x,
                                                                         event.pos[1] - base_y))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    text_box.text_box_layout.set_text_selection(48, 245)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    text_box.text_box_layout.set_text_selection(56, 220)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    text_box.text_box_layout.set_text_selection(0, 5)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    text_box.text_box_layout.set_text_selection(0, 4)
                
                manager.process_events(event)
                

            manager.update(UI_REFRESH_RATE)

            row_key_pos = 13
            typing_row = len(text_box.text_box_layout.layout_rows) - 1
            cursor_toggle = 0

            text_box.scroll_bar.has_moved_recently = True
            text_box.update(5.0)
            text_box.set_active_effect(pygame_gui.TEXT_EFFECT_BOUNCE, effect_tag='test')
            cursor_toggle += UI_REFRESH_RATE
            if cursor_toggle >= 0.4:
                cursor_toggle = 0.0
                text_box.text_box_layout.toggle_cursor()
                text_box.redraw_from_text_block()

            SCREEN.fill((211, 211, 211))
            textname = font.render("Enter Name", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 300))
            textname = font.render("Enter Number", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 350))
            textname = font.render("Search Name", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 100))
            textname = font.render(number, True, (96, 96, 96))
            SCREEN.blit(textname, (250, 150))
            manager.draw_ui(SCREEN)
            pygame.display.update()
        
    username()

if name == "main":
    main()
