class Medusa:
  def __init__(self, name, statues = []):
    self.name = name
    self.statues = statues

  def stare(self, victim):
    # if len(self.statues) < 3:
    if len(self.statues) == 3:
      self.statues[0].stoned = False
      self.statues.pop(0)
      self.statues.append(victim)
      victim.stoned = True
    else:
      self.statues.append(victim)
      victim.stoned = True



class Person:
  def __init__(self, name, stoned = False):
    self.name = name
    self.stoned = stoned

  def is_stoned(self):
    return self.stoned