class Hobbit:
  def __init__(self, name, disposition = "homebody"):
    self.name = name
    self.disposition = disposition
    self.age = 0

  def celebrate_birthday(self):
    self.age += 1

  def is_adult(self):
    return self.age > 32

  def is_old(self):
    return self.age >= 101

  def has_ring(self):
    if self.name == "Frodo":
      return True

  def is_short(self):
    return True