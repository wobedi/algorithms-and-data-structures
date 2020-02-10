from pandas import DataFrame

from src.symbol_tables import config


class HashMap:
  def __init__(self, size):
    self.size = size
    self.table = [[] for i in range(size)]  # list of lists implements chaining
    self.load = 0

  def __str__(self):
    return f'{self.table} | size: {self.size} | load: {self.load}'

  def put(self, key, value):
    row = self.table[self.modular_hash(key)]
    for tup in row:
      if tup[0] == key:
        tup[1] = value
        return
    row.append((key, value))
    self.load += 1
    if self.load / self.size >= config.chaining['LOAD_FACTOR_MAX']:
      self.upsize()
    return 

  def get(self, key):
    row = self.table[self.modular_hash(key)]
    if len(row) < 0:
      return print(f'\nKey {key} not in table')
    for tup in row:
      if tup[0] == key:
        return print(tup[1])
    
  def delete(self, key):
    row = self.table[self.modular_hash(key)]
    if len(row) <= 0:
      return print(f'\nKey {key} not in table')
    for i, tup in enumerate(row):
      if tup[0] == key:
        del row[i]
        self.load -= 1
        if self.load / self.size <= config.chaining['LOAD_FACTOR_MIN']:
          self.downsize()
        return

  def modular_hash(self, key):
    return hash(key) % self.size

  def downsize(self):
    return self.resize(config.chaining['DOWNSIZE_FACTOR'])
  
  def upsize(self):
    return self.resize(config.chaining['UPSIZE_FACTOR'])

  def resize(self, factor):
    self.size = int(self.size * factor)
    aux_table = [[] for i in range(self.size)]
    for row in self.table:
      for k, v in row:
        aux_table[self.modular_hash(k)].append((k, v))
    self.table = aux_table
    return


# Turn this into a unit test
if __name__ == '__main__':
  HT = HashMap(5)
  print(DataFrame(HT.table))
  HT.get("hello")
  print(DataFrame(HT.table))
  HT.put("hello", "hellov")
  print(DataFrame(HT.table))
  HT.get("hello")
  print(DataFrame(HT.table))
  HT.put(1, "1v")
  print(DataFrame(HT.table))
  HT.put(2, "2v")
  print(DataFrame(HT.table))
  HT.put(3, "3v")
  print(DataFrame(HT.table))
  HT.put(4, "4v")
  print(DataFrame(HT.table))
  HT.put(5, "5v")
  print(DataFrame(HT.table))
  HT.put(6, "6v")
  print(DataFrame(HT.table))
  HT.put(7, "7v")
  print(DataFrame(HT.table))
  HT.delete(7)
  print(DataFrame(HT.table))
  HT.delete(7)
  print(DataFrame(HT.table))
  HT.delete(5)
  print(DataFrame(HT.table))
  HT.delete(3)
  print(DataFrame(HT.table))
  HT.delete(2)
  print(DataFrame(HT.table))
  HT.delete(4)
  print(DataFrame(HT.table))
  HT.delete("hello")
  print(DataFrame(HT.table))
  HT.delete(1)
  print(DataFrame(HT.table))