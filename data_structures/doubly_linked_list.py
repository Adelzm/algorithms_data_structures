class NodeD:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

  def __str__(self):
    next_value = self.next.value if self.next else None
    prev_value = self.prev.value if self.prev else None

    return f"Node(value: {self.value}, prev: {prev_value}, next: {next_value})"

class DoublyLinkedList:
  def __init__(self, value):
    new_node = NodeD(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1


  def print_list(self):
    current = self.head
    while current:
      print(current)
      current = current.next

  def append(self, value):
    new_node = NodeD(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1


