import json
import re
from ganjoor import Ganjoor, Poem


RHYTHMS: dict[str, dict] = {}
with open('arouz.json') as file:
    RHYTHMS = json.load(file)

class GanjoorAPI(Ganjoor):
  def __init__(
    self, 
    token=None, 
    language="string", 
    app_name="pythonclient"):
   super().__init__(token, language, app_name)
  
  def get_poem(self):
    poem = self.hafez_faal()
    notation, rhythm = self.get_rhythm(poem)
    return {'notation': notation, 'rhythm':rhythm, 'firstBeyt': self.get_first_beyt(poem)}

  def get_rhythm(self, poem: Poem):
    r = re.sub("\s*\(.+\)\s*", "", poem._sections[0]['ganjoorMetre']['rhythm'])
    if r not in RHYTHMS:
      raise ValueError(f"Not implemented: {r}")
    return r, RHYTHMS[r]


  def get_first_beyt(self, poem: Poem):
    return poem._plain_text.split('\n')[0]


 

if __name__ == '__main__':
  g = GanjoorAPI()
  print(g.get_poem())
  
