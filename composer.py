import numpy as np
from models import FREQUENCIES, Notes, Dastgah, Ava
from ganjoor_interface import GanjoorAPI


class Composer:
    # This is a very basic implementation of a composer.
    # In a real implementation, this would be much more 
    # complex and would take into account the
    # characteristics of each Dastgah, the structure of the poem, etc.

    def melody(self):
        return np.random.choice(a=["U","D", "-"], p=[0.3, 0.3, 0.4], size=1)

    def jump(self):
        return np.random.choice(a=["5","4"], p=[0.5, 0.5], size=1)

    def progres(self, n):
        prog = np.random.choice(a=[self.melody, self.jump], p=[.9,.1], size=1)
        match prog[0]():
            case "-":
                return np.append(arr=n, values=n[-1])
            case "U":
                if Notes.i(n[-1]) == 7:
                    return np.append(arr=n, values=Notes.down(n[-1]))  
                return np.append(arr=n, values=Notes.up(n[-1]))
            case "D":
                if Notes.i(n[-1]) == 0:
                    return np.append(arr=n, values=Notes.up(n[-1]))  
                return np.append(arr=n, values=Notes.down(n[-1]))
            case "5":
                if Notes.i(n[-1]) == 1:
                    return np.append(arr=n, values=Notes.p5(n[-1]))
                return np.append(arr=n, values=Notes.up(n[-1]))  
            case "4":
                if Notes.i(n[-1]) == 1:
                    return np.append(arr=n, values=Notes.p4(n[-1]))
                return np.append(arr=n, values=Notes.up(n[-1]))



class Song:
    def __init__(self, dastgah: str) -> None:
        self.dastgah: Dastgah = Dastgah(dastgah) # shur D
        self.poem = GanjoorAPI().get_poem()
        self.arouz: str = self.poem['rhythm']['arouz']
        self.rhythm: str = self.poem['rhythm']['r']
        print(f"Poem: {self.poem.get('firstBeyt')}")
        print(f"Arouz: {self.poem.get('notation')}")
        print(f"Rhythm: {self.length + 1}/16")

    @staticmethod
    def _translate(k: str) -> list[Ava]:
        if k == '/': return [Ava.L]
        if k == 'X': return [Ava.S, Ava.L]
        if k == '%': return [Ava.S, Ava.S, Ava.L]
        

    def get_rhythm(self) -> list[Ava]:
        return sum([self._translate(s) for s in self.rhythm], [])
        
    @staticmethod
    def duration(s: str):
        if s=="/": return 2
        if s=="X": return 3
        if s=="%": return 4


    @property
    def length(self) -> int:
        return sum([self.duration(s)  for s in self.rhythm])


    def get_melody(self) -> list[Ava]:
        c = Composer()
        melody = []
        n = self.first_note(self.dastgah.init_weights)
        for r in self.get_rhythm():
            n = c.progres(n)
            melody.append({'note': n[-1], 'duration':r})
        return melody



    def first_note(self, weights: list[float]) -> str:
        return np.random.choice(a=Notes.n, p=weights, size=1)
