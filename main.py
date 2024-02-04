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
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from chordProgression import ChordProgression

class MakeButton(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_touch_down(self, touch):
        if not(self.collide_point(*touch.pos) and touch.button == 'left'):
            return super().on_touch_down(touch)
      
        self.md_bg_color = .13, .13, .13, .2
        
        numberChords = self.parent.getNumberOfChords()
        rootNote, mode = self.parent.getScale()

        #clear all buttons
        for i in range(8):
            self.parent.ids[f'btn{i}'].ids.chord.text = ''

        if numberChords == 0: 
            return
        
        chords = ChordProgression(rootNote, mode, numberChords)
        chordsStr = [' '.join(i) for i in chords.getChordProgression()]
        

        for i in range(len(chordsStr)):
            self.parent.ids[f'btn{i}'].ids.chord.text = chordsStr[i]
            

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
    
    def disableButton(self, btn) -> None:
        _btn = self.ids[f'btn{btn}']
        _prev_btn = self.ids[f'btn{btn - (btn > 0)}']
        _next_btn = self.ids[f'btn{btn + (btn < 7)}']

        if _btn.state == 'down':
            if _prev_btn.state != 'down':
                _btn.state = 'normal'    

        if _btn.state == 'normal':
            if _next_btn.state == 'down':
                _btn.state = 'down' 

    def getNumberOfChords(self) -> int:
        count = 0
        for i in range(8):
            btn = self.ids[f'btn{i}']
            count += (btn.state == 'down')
        return count
    
    def getScale(self) -> tuple:
        parent = self.ids.scaleSelector.ids
        rootNote = parent.rootNote.text
        mode = parent.mode.text

        return rootNote, mode
    
class ChordMaker(MDApp):

    def builder(self):
        return MainView()

if __name__ == '__main__':
    LabelBase.register(name='Cabin Sketch', fn_regular='src/CabinSketch.ttf')
    ChordMaker().run()