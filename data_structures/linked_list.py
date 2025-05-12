class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next is not None:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True

  def print_list(self):
    current = self.head
    while current is not None:
      print(current)
      current = current.next

  def find_middle_node(self):
        fast = self.head
        slow = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next if fast and fast.next else None
        
        return slow


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __str__(self):
    next_value = self.next.value if self.next else None
    return f"Node(value: {self.value}, next: {next_value})"


def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow