# The functions associated with stack are:
# empty() – Returns whether the stack is empty
# size() – Returns the size of the stack
# top() – Returns a reference to the topmost element of the stack
# push(a) – Inserts the element ‘a’ at the top of the stack
# pop() – Deletes the topmost element of the stack

from inspect import stack


stack = []

stack.insert(0, 1)
stack.insert(0, 2)
stack.insert(0, 3)
stack.insert(0, 4)
stack.pop()
print(stack)
