import os
import numpy as np
import wavio# Parameters
from helpers import deb_pr
from composer import Song
from models import FREQUENCIES
from models import Ava



class Audio:
    def __init__(self, melody: list[Ava]) -> None:
        self.melody = melody
        self.RATE = 44100


    def generate_tone(self, freq, duration=0.5):
        # add tempo for duration
        t = np.linspace(0, duration, int(self.RATE * duration), False)
        tone = np.sin(freq * t * 2 * np.pi)
        return self.fade_note(tone)


    def fade_note(self, note, fade_duration=0.01):
        fade_samples = int(self.RATE * fade_duration)
        fade_in = np.linspace(0, 1, fade_samples)
        fade_out = np.linspace(1, 0, fade_samples)
        note[:fade_samples] *= fade_in
        note[-fade_samples:] *= fade_out
        return note


    def get_sound(self, note_array: list[dict]):
        audio = np.array([])
        for n in note_array:
            a = self.generate_tone(freq=FREQUENCIES[n['note']], 
                                   duration=n['duration'].value)
            audio = np.append(audio, a)
        wavio.write("sample.wav", audio, self.RATE, sampwidth=3)


    def lilylize(self, piece: str, rythem: int, dastgah: str, tempo: int, title: str):
        # add tempo, dastgah, and other necessary information to the piece
        header = f"\\header {{title = \\markup {{ \\bold {{ {title} }} }}}} \n"
        pre_lily = '\\version "2.24.3"\n\\include "persian.ly"\n'
        lily = 'piece = \\relative {\n\\autoBeamOff\n'
        lily += f'\\time {rythem}/16\n'  
        lily += f'\\tempo 8 = {tempo}\n'
        lily += piece[0]+"'"+piece[1:] + '\n}\n'
        post_lily = '\\score { \\piece }'
        with open("score.ly", "w") as f:
            f.write(header + pre_lily + lily + post_lily)



    def write_note(self, note_array: list[dict], rythem: int, dastgah: str, tempo: int, title: str):
        piece = " ".join([f"{str(n['note'])}{n['duration'].name}" for n in  note_array]).replace("L", "16.").replace("S", "16")
        self.lilylize(piece, rythem, dastgah, tempo, title)
        os.system("docker run -v $(pwd):/workdir -w /workdir codello/lilypond score.ly")

