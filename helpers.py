
def lilypond_wrapper(string: str, rythem: int):
  pre_lily = '\\version "2.24.3"\n\\include "persian.ly"\n'
  lily = 'piece = \\relative {\n\\autoBeamOff\n'
  lily += f'\\time {rythem}/8\n'  
  lily += string[0]+"'"+string[1:] + '\n}\n'
  post_lily = '\\score { \\piece }'

  with open("tmp.ly", "w") as f:
    f.write(pre_lily + lily + post_lily)


def deb_pr(s):
  print('DEBUG LOG'+"-"*10); print(s); print("-"*10)
  
