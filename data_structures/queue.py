class NodeQ:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __str__(self):
    next_value = self.next.value if self.next else None
    return f"Node(value: {self.value}, next: {next_value})"

class Queue:
  def __init__(self, value):
    new_node = NodeQ(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

  def print_queue(self):
    current = self.first
    while current is not None:
      print(current)
      current = current.next

  def enqueue(self, value):
    new_node = NodeQ(value)
    if self.length == 0:
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1

  def dequeue(self):
    if self.length == 0:
      print("Nothing to pope")
      return None
    temp = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = temp.next
      temp.next = None
    self.length -= 1
    return temp