from typing import Union
import matplotlib.pyplot as plt
from enum import Enum
import numpy as np

class NOTE(Enum):
    C = 0
    D = 1
    E = 2
    F = 3
    G = 4
    A = 5
    B = 6
    

class Notes:
    n: list[NOTE] = ["c", "d", "e", "f", "g", "a", "b"]
    
    @classmethod
    def i(self, m):
        return self.n.index(m)

    @classmethod
    def up(self, m):
        return self.n[(self.i(m) + 1)%7]

    @classmethod
    def down(self, m):
        return self.n[(self.i(m) - 1)%7]

    @classmethod
    def p5(self, m):
        return self.n[(self.i(m) +4 )%7]

    @classmethod
    def p4(self, m):
        return self.n[(self.i(m) +3 )%7]
    
    @classmethod
    def melody_plot(self, m: list[NOTE], *arg, **kwargs):
        fig, ax = plt.subplots()
        ax.plot(m, *arg, **kwargs)
        print(Notes.n)
        ax.set_yticks(range(len(Notes.n)), Notes.n)
        return fig, ax
                


class D(Enum):
    Shur = 1
    Chargah = 2
    Segah = 3
    Nava = 4
    RastPanjgha = 5
    Mahour = 6
    Homayoun = 7

class Dastgah:
    def __init__(self, name: D) -> None:
        self.name = name
 
    @property
    def init_weights(self) -> list[float]:
        # This is a placeholder. In a real implementation, 
        # these weights would be based 
        # on the characteristics of each Dastgah.
        match self.name:
            case 'Shur':
                weights = [1,1,1,1,1,1,1]
            case 'Mahur':
                weights = [1,1,1,1,1,1,1]
            case 'Segah':
                weights = [1,1,1,1,1,1,1]
            case 'Nava':
                weights = [1,1,1,1,1,1,1]
            case 'RastPanjgha':
                weights = [1,1,1,1,1,1,1]
            case 'Homayoun':
                weights = [1,1,1,1,1,1,1]
        return weights / np.sum(weights)
    


class Ava(Enum):
    S = 2 # ta -> short
    L = 3 # tan -> long
    XL = 4 # tan -> long




FREQUENCIES = {
    "c": 261.63, "cs": 277.18 , "db": 277.18,
    "d": 293.66, "ds":311.13, "eb": 311.13,
    "e": 329.63,
    "f": 349.23, "fs": 369.99, "gb":369.99,
    "g": 392.00, "gs": 415.30, "ab": 415.,
    "a": 440.00, "as": 466.16, "bb": 466.16,
    "b": 493.88
}