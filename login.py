import pygame as pg
import pygame_gui as pg_gui
from MeowerBot import Client

pg.font.init()

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('lightskyblue3')
        self.start_text = text
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                
                if event.key == pg.K_BACKSPACE:
                    if len(self.text) == 0:
                        self.text = self.start_text
                    else:
                        self.text = self.text[:-1]
                
                else:
                    if __file__ == "login.py" and self.start_txt == "password":
                        self.text += "*"
                    else:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, pg.Color('#000000'))
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

    def kill(self):
        self.rect.kill()


def login_prompt(mngr, surface, background):
    #800 600
    psswrd_input = InputBox((800/2) - 55 ,600/2+50, 200 ,55 , "password")
    username_input= InputBox((800 / 2 ) - 55 , 600/2, 200, 55, "username")
    submit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect(0,600 /2 + 70  ,400/2 , 55), text= "login", manager=mngr)

    
    clock = pg.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                __import__("sys").exit()
            psswrd_input.handle_event(event)
            username_input.handle_event(event)
    #        if event.type == pg_gui.UI_BUTTON_PRESSED:
    #          if event.ui_element == hello_button:
    #               print('Hello World!')
            if event.type == pg_gui.UI_BUTTON_PRESSED:
                if event.ui_element == submit_button:
                    is_running = False
            mngr.process_events(event)

        mngr.update(time_delta)

        surface.blit(background, (0, 0))
        psswrd_input.draw(screen=surface)
        username_input.draw(screen=surface)
        mngr.draw_ui(surface)

        pg.display.update()
        pg.display.flip()
    submit_button.kill()

    return Client(username_input.text,psswrd_input.text,debug=False)

