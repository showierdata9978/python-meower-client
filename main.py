from threading import Thread

import pygame as pg 
import pygame_gui as pg_gui

from MeowerBot import Client, CantConnectError

from login import login_prompt,InputBox
from Client import setup
pg.init()

pg.display.set_caption('Quick Start')
window_surface = pg.display.set_mode((800, 600))

background = pg.Surface((800, 600))
background.fill(pg.Color('#e77f00'))

manager = pg_gui.UIManager((800, 600))

client = login_prompt(manager, window_surface, background)
setup(client)
send_button = pg_gui.elements.UIButton(relative_rect=pg.rect.Rect((800 - 150,0), (150 ,55)), text="send", manager=manager)
send_text = InputBox(0 ,0,800-150 ,55 , "Send Something")
clock = pg.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
           is_running = False
        send_text.handle_event(event)
        if event.type == pg_gui.UI_BUTTON_PRESSED:
           if event.ui_element == send_button:
                client.send_msg(send_text.text)
                send_text.text = ""
            
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    send_text.draw(screen=window_surface)
    manager.draw_ui(window_surface)

    pg.display.update()
    pg.display.flip()
