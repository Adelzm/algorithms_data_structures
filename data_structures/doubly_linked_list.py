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
    return True

  def pop(self):
    if self.length == 0:
      print("Nothing to pope")
      return None
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = temp.prev
      self.tail.next = None
      temp.prev = None
    self.length -= 1
    return temp
  
  def prepend(self, value):
    new_node = NodeD(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True

  def pop_first(self):
    if self.length == 0:
      print("Nothing to pope")
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = temp.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp
  
  def get(self, index):
    # First, handle edge cases
    if index < 0 or index >= self.length:
      print("Out of range")
      return None
    # Second: iterate over the list, while taking advantage of double link (prev) to make it more efficient
    temp = self.head
    if index < self.length / 2:
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
    
    return temp

  def set_value(self, index, value):
    node_to_change = self.get(index)

    if node_to_change:
      node_to_change.value = value
      return True
    
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    
    new_node = NodeD(value)
    before = self.get(index - 1)
    after = before.next
    before.next = new_node
    new_node.prev = before
    after.prev = new_node
    new_node.next = after

    self.length += 1
    return True
  
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    
    temp = self.get(index)

    before = temp.prev
    after = temp.next
    before.next = after
    after.prev = before
    temp.prev = None
    temp.next = None

    self.length -= 1
    return temp
    

     

     
     








