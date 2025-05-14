class NodeS:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __str__(self):
    next_value = self.next.value if self.next else None
    return f"Node(value: {self.value}, next: {next_value})"
  
  class Stack:
    def __init__(self, value):
      new_node = NodeS(value)
      self.top = new_node
      self.height = 1


    def print_stack(self):
      current = self.top
      while current is not None:
        print(current)
        current = current.next

    def push(self, value):
      new_node = NodeS(value)
      if self.height == 0:
        self.top = new_node
      else:
        new_node.next = self.top
        self.top = new_node
      self.height += 1
      return True
    
    def pop(self):
      if self.height == 0:
        return None
      temp = self.top
      if self.height == 1:
        self.top = None
        temp.next = None
      else:
        self.top = temp.next
        temp.next = None
      self.height -= 1
      return temp