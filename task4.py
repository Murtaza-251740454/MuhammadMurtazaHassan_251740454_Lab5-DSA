from task1 import Stack

def isBalanced(s):
    st = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in "({[":
            st.push(c)
        elif c in ")}]":
            if st.is_empty():
                return False
            top = st.peek()
            if top != pairs[c]:
                return False
            st.pop()


    return st.is_empty()


if __name__ == "__main__":
    tests = ["[()()]"]
    print("True"if isBalanced(tests) else "False")
    