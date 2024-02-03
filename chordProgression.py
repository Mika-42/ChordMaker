# ------------------------------------------------------------------------------
#   project: chord generator
#
#   author: matis
# ------------------------------------------------------------------------------
import random

class ChordProgression:

    def __init__(self, rootNote: str, mode: str, chordNumber: int = 4):

        notes: dict = ['C', 'C#', 'D', 'D#',
                       'E', 'F', 'F#', 'G',
                       'G#', 'A', 'A#', 'B']

        if rootNote not in notes:
            return

        if mode not in ['maj', 'min']:
            return

        if chordNumber < 2:
            return

        circle: dict = {
            'maj': ['C', 'G', 'D', 'A', 'E',  'B',
                    'F#', 'C#', 'G#', 'D#', 'A#', 'F'],

            'min': ['A', 'E',  'B', 'F#', 'C#', 'G#',
                    'D#', 'A#', 'F', 'C', 'G', 'D'],
        }

        self.rootNote: str = notes.index(rootNote)
        self.mode: str = mode
        self.chordNumber: int = chordNumber
        self.relMode: str = 'maj' if mode == 'min' else 'min'
        self.scale: list = [
            (circle[self.mode][self.rootNote], self.mode),
            (circle[self.relMode][self.rootNote - 1], self.relMode),
            (circle[self.relMode][self.rootNote + 1], self.relMode),
            (circle[self.mode][self.rootNote - 1], self.mode),
            (circle[self.mode][self.rootNote + 1], self.mode),
            (circle[self.relMode][self.rootNote], self.relMode),
            (circle[self.relMode][self.rootNote + 2], 'dim'),
        ]

        self.chordProgression: list = []

        for i in range(self.chordNumber):
            self.chordProgression.append(random.choice(self.scale))

    def getScale(self) -> list:
        return self.scale

    def getRootNote(self) -> str:
        return self.rootNote

    def getMode(self) -> str:
        return self.mode

    def getChordNumber(self) -> int: return self.chordNumber

    def getChordProgression(self) -> list: return self.chordProgression

    def __str__(self) -> str:
        out = f'root note: {self.rootNote}\n'
        out += f'mode: {self.mode}\n'
        out += f'scale: {self.scale}\n'
        out += f'number of chords: {self.chordNumber}\n'
        out += f'chord progression: {self.chordProgression}'

        return out

    def changeChord(self, pos : int):
        if not(0 <= pos < self.chordNumber - 1):
            return 
        
        self.chordProgression[pos] = random.choice(self.scale)

