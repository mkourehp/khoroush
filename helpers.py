from bidi.algorithm import get_display
import arabic_reshaper


def farsi(s):
  return get_display(arabic_reshaper.reshape(s))

def deb_pr(s):
  print("-"*10 + 'DEBUG  LOG'+"-"*10); print(s); print("-"*30)
  
