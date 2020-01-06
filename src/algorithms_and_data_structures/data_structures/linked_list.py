class ListItem:
  # TODO: this vs stack vs queue...
  # TODO Add LinkedList class & refactor this
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def all(self):
    res = []
    item = self
    while item is not None:
      res.append(item.value) if item.value is not None else None
      item = item.next
    return res

  def contains(self, value):
    item = self
    while item is not None:
      if item.value == value:
        return True
      item = item.next
    return False

  def count(self):
    count = 0
    item = self
    while item.next is not None:
      count += 1
      item = item.next
    return count

  def final(self):
    item = self
    while item.next is not None:
      item = item.next
    return item