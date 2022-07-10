class intSet(object):
  def __init__(self):
    self.vals = []
  
  def insert(self, e):
    if not e in self.vals:
      self.vals.append(e)
  
  def member(self, e):
    return e in self.vals
  
  def remove(self, e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(f'{e} not found')
  
  def __str__(self):
    self.val.sort()
    result = ''
    for e in self.vals:
      result += f'{e},'
    return '{' + result[:-1] + '}'