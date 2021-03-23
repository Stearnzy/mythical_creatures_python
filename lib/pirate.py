class Pirate:
  def __init__(self, name, job = 'Scallywag'):
    self.name = name
    self.job = job
    self.action_count = 0
    self.booty = 0

  def is_cursed(self):
    if self.action_count >= 3:
      return True

  def commit_heinous_act(self):
    self.action_count += 1

  def rob_ship(self):
    self.booty += 100