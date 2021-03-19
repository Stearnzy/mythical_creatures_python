class Ogre:
  def __init__(self, name, home = 'Swamp'):
    self.name = name
    self.home = home
    self.swings = 0

  def encounter(self, human):
    human.encounter_counter += 1
    if human.encounter_counter % 3 == 0:
      self.swings += 1
      human.hit_count += 1
      if human.hit_count == 2:
        human.knocked_out = True

  def swing_at(self, human):
    self.swings += 1

  def apologize(self, human):
    human.knocked_out = False
    human.hit_count = 0


class Human:
  def __init__(self, name = 'Jane'):
    self.name = name
    self.encounter_counter = 0
    self.hit_count = 0
    self.knocked_out = False
  
  def notices_ogre(self):
    return self.encounter_counter >= 3
