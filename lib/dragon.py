class Dragon:
  def __init__(self, name, color, rider):
    self.name = name
    self.color = color
    self.rider = rider
    self.meals = 0

  def is_hungry(self):
    return self.meals < 3

  def eat(self):
    self.meals += 1