import os
import numpy as np
import wavio# Parameters
from helpers import deb_pr, lilypond_wrapper
from main import S
from models import FREQUENCIES

RATE = 44100    # samples per second

def single_note(note: str, duration):
  d = duration.value / 5
  try:
    f = FREQUENCIES[note]
  except KeyError:
    raise ValueError(f'Note {note} not defined!')
  t = np.linspace(0, d, int(d*RATE), endpoint=False)
  return np.sin(2*np.pi * f * t)# Write the samples to a file



def get_sound(note_array: list[dict]):
  audio = np.array([])
  for n in note_array:
    a = single_note(note=str(n['note']), duration=n['duration'])
    audio = np.append(audio, a)
  wavio.write("sample.wav", audio, RATE, sampwidth=3)


def music():
  s = S('Mahur')
  m = s.get_melody()
  return {'music':m, 'rythem': s.length}


def write_note(note_array: list[dict], rythem: int):
  piece = " ".join([f"{str(n['note'])}{n['duration'].name}" for n in  note_array]).replace("L", "8.").replace("S", "8")
  deb_pr(lilypond_wrapper(piece, rythem))
  os.system("docker run -v $(pwd):/workdir -w /workdir codello/lilypond tmp.ly")


if __name__ == "__main__":
  m = music()
  get_sound(m['music'])
  write_note(m['music'], m['rythem'])
