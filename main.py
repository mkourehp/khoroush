from models import D, FREQUENCIES, Ava, Notes, Dastgah
import numpy as np


class Lilyize:
    def __init__(self, rytheme: list[Ava], ) -> None:
        pass

class Composer:
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

class S:
    def __init__(self, dastgah: str) -> None:
        self.arouz: str = "مفعول و مفاعیل و مفاعیل و فعل"
        self.dastgah: Dastgah = Dastgah(dastgah) # shur D
        self.rytheme: str = r"//%/%/%" # -> should be enum

    @staticmethod
    def _translate(k: str) -> list[Ava]:
        if k == '/': return [Ava.L]
        if k == 'X': return [Ava.S, Ava.L]
        if k == '%': return [Ava.S, Ava.S, Ava.L]
        

    def get_rytheme(self) -> list[Ava]:
        return sum([self._translate(s) for s in self.rytheme], [])
        
    @staticmethod
    def duration(s: str):
        if s=="/": return 2
        if s=="X": return 3
        if s=="%": return 4


    @property
    def length(self) -> int:
        return sum([self.duration(s)  for s in self.rytheme])


    def get_melody(self) -> list[Ava]:
        c = Composer()
        n = self.first_note(self.dastgah.init_weights)
        for i in range(len(self.get_rytheme())):
            n = c.progres(n)
        return n


    def weights_normalizer(self, weights: list[float]) -> list[float]:
        normal_factor = sum(weights)
        return np.array(weights)/normal_factor

    def first_note(self, weights: list[float]) -> str:
        weights = self.weights_normalizer(weights)
        return np.random.choice(a=Notes.n, p=weights, size=1)


    @staticmethod
    def get_freq(s: str):
        return FREQUENCIES[s]


if __name__ == "__main__":
    print(S().get_rytheme())

