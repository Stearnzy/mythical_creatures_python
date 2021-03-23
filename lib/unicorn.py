class Unicorn:
  def __init__(self, name, color = 'white'):
    self.name = name
    self.color = color

  def is_white(self):
    if self.color == 'white':
      return True 

  def say(self, string):
    return f'**;* {string} **;*'