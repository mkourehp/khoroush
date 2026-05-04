from composer import Song
from audio import Audio

if __name__ == "__main__":
  song = Song("Mahur")
  m = song.get_melody()
  audio = Audio(m)
  audio.get_sound(m)
  audio.write_note(m, song.length)
