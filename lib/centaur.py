class Centaur:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    self.action_count = 0
    self.standing = True

  def shoot(self):
    self.action_count += 1
    if self.is_cranky() == False and self.standing == True:
      return "Twang!!!"
    else:
      return "NO!"

  def run(self):
    self.action_count += 1
    if self.is_cranky() == False and self.standing == True:
      return "Clop clop clop clop!!!"
    else:
      return "NO!"

  def is_cranky(self):
    return self.action_count >= 3

  def is_standing(self):
    return self.standing

  def sleep(self):
    if self.is_standing():
      return "NO!"
    else:
      self.action_count = 0

  def lay_down(self):
    self.standing = False

  def is_laying(self):
    return not self.standing

  def stand_up(self):
    self.standing = True

  def drink_potion(self):
    if self.action_count == 0 and self.is_standing():
      return "Now I'm sick"
    elif self.action_count >= 1 and self.is_standing():
      self.action_count = 0
    else:
      return "Can't, I'm laying"