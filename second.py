class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        removed = self.stack.pop()
        print(f"Popped {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top of stack: {self.stack[-1]}")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)