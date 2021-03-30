class Wizard:
  def __init__(self, name, bearded = True):
    self.name = name
    self.bearded = bearded
    self.cast_count = 0

  def is_bearded(self):
    return self.bearded

  def incantation(self, message):
    return f"sudo {message}"

  def is_rested(self):
    if self.cast_count < 3:
      return True

  def cast(self):
    self.cast_count += 1
    return "MAGIC MISSILE!"