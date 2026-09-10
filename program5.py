stack = []

def push():
    element = input("Enter an element to push onto the stack: ")
    stack.append(element)
    print("Element pushed:", element)

def pop():
    if not stack:
      print("Stack is empty!")
    else:
        print("Popped element:", stack.pop())

def peak():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack elements:", stack)

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peak")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peak()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")