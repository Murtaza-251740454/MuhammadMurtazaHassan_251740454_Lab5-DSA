from task1 import Stack

def reverse(s):
    stack = Stack()
    for i in s:
        stack.push(i)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

print("Original Text: Hello World")
print("Reversed Text:",reverse("Hello World"))