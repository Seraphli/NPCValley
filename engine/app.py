import pygame
from pygame.locals import *
from engine.event import GEvent


class GAPP(GEvent):
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()
            self._running = False

        elif event.type >= USEREVENT:
            self.on_user(event)

        elif event.type == VIDEOEXPOSE:
            self.on_expose()

        elif event.type == VIDEORESIZE:
            self.on_resize(event)

        elif event.type == KEYUP:
            self.on_key_up(event)

        elif event.type == KEYDOWN:
            self.on_key_down(event)

        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 0:
                self.on_lbutton_up(event)
            elif event.button == 1:
                self.on_mbutton_up(event)
            elif event.button == 2:
                self.on_rbutton_up(event)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 0:
                self.on_lbutton_down(event)
            elif event.button == 1:
                self.on_mbutton_down(event)
            elif event.button == 2:
                self.on_rbutton_down(event)

        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()
