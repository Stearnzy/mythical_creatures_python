class Vampire:
  def __init__(self, name, pet = 'bat'):
    self.name = name
    self.pet = pet
    self.thirsty = True

  def is_thirsty(self):
    return self.thirsty

  def drink(self):
    self.thirsty = False