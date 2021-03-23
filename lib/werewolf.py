class Werewolf:
  def __init__(self, name, location = None, human_state = True, hungry = False):
    self.name = name
    self.location = location
    self.human = human_state
    self.hungry = hungry

  def is_human(self):
    return self.human

  def is_wolf(self):
    return not self.human

  def change(self):
    self.human = not self.human
    self.hungry = True

  def is_hungry(self):
    return self.hungry

  def consume(self, human):
    if self.human != True:
      self.hungry = False
      human.status = "Dead"
    else:
      return "No one was consumed"



class Victim:
  def __init__(self):
    self.status = "Alive"