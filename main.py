# ------------------------------------------------------------------------------
#   project: chord generator
#
#   author: matis
#
#   src: https://composer-sa-musique.fr/cycle-des-quintes-le-guide-ultime
#        -3-4-creer-des-suites-daccords-avec-le-cycle/
# ------------------------------------------------------------------------------
import kivy
kivy.require('2.1.0') 

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '450')

from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
#from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.widget import MDWidget

class MakeButton(MDBoxLayout):
    def on_touch_down(self, touch):
        if not(self.collide_point(*touch.pos) and touch.button == 'left'):
            return super().on_touch_down(touch)
        
        self.md_bg_color = .13, .13, .13, .2
        
        
        return super().on_touch_down(touch)

class ChordButton(MDFlatButton, MDToggleButton):
    pass

class ScaleSelector(MDBoxLayout):
    pass
   
class RootNoteLabel(MDLabel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentNoteIndex = 0
        self.notes = ['C', 'C#', 'D', 'D#',
                       'E', 'F', 'F#', 'G',
                       'G#', 'A', 'A#', 'B']
        
    def on_touch_down(self, touch):

        if touch.is_mouse_scrolling and self.collide_point(*touch.pos):
            if touch.button == 'scrollup':
                self.currentNoteIndex -= 1

                if self.currentNoteIndex < 0:
                    self.currentNoteIndex = 11

            elif touch.button == 'scrolldown':
                self.currentNoteIndex += 1

                if self.currentNoteIndex > 11:
                    self.currentNoteIndex = 0

        self.text = self.notes[self.currentNoteIndex]

        super().on_touch_down(touch)
    
class ModeLabel(MDLabel):
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentModeIndex = 0
        self.mode = ('maj', 'min')
        
    def on_touch_down(self, touch):

        if touch.is_mouse_scrolling and self.collide_point(*touch.pos):
            if touch.button in ('scrollup', 'scrolldown'):
                    self.currentModeIndex = not self.currentModeIndex

        self.text = self.mode[self.currentModeIndex]

        super().on_touch_down(touch)
     
class MainView(MDScreen):
    
    def disableButton(self, btn):
        _btn = self.ids[f'btn{btn}']
        _prev_btn = self.ids[f'btn{btn - (btn > 0)}']
        _next_btn = self.ids[f'btn{btn + (btn < 7)}']

        if _btn.state == 'down':
            if _prev_btn.state != 'down':
                _btn.state = 'normal'    

        if _btn.state == 'normal':
            if _next_btn.state == 'down':
                _btn.state = 'down' 

class ChordMaker(MDApp):

    def builder(self):
        return MainView()

if __name__ == '__main__':
    LabelBase.register(name='Cabin Sketch', fn_regular='src/CabinSketch.ttf')
    ChordMaker().run()