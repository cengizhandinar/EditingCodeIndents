import re
class ArrayStack:
  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)

  def is_empty(self):
    return len(self._data) == 0

  def push(self, e):
    self._data.append(e)

  def top(self):
    if self.is_empty():
      return False
    return self._data[-1]

  def pop(self):
    if self.is_empty():
      return False
    return self._data.pop()
  def printStack(self):
    print(self._data)

S1 = ArrayStack()
source = open("main.c","r")
changed = open("changed.c","w")
counter = 0
while(True):
    line = source.readline()
    if(line=="}"):
        S1.push(line)
        changed.write(S1.pop())
        break
    elif(line == "{\n"):
        S1.push("\t" * counter + line)
        changed.write(S1.pop())
        counter += 1
    elif(line == "}\n"):
        counter -= 1
        S1.push("\t" * counter + line)
        changed.write(S1.pop())
    else:
        S1.push("\t" * counter + line)
        changed.write(S1.pop())

source.close()
changed.close()




