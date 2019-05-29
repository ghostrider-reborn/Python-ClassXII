"""
    STACKS
"""

# Initialize an empty stack as a python list
top = None
stack = []

def push(stack, element):
    ''' Push an element into a stack '''
    global top
    stack.append(element)
    top = len(stack) - 1

def pop(stack):
    ''' Remove the top element of the stack '''
    global top
    if top is None: return False
    
    stack.pop()
    if stack == []: top = None
    else: top = len(stack) - 1

def peek(stack):
    ''' Return the top element of the stack '''
    global top
    return stack[top] if top is None else "Underflow error!"

def display(stack):
    ''' Display the contents of the stack '''
    global top
    if top is None:
        print("Underflow error!")
        return
    
    print(stack[top], "<- top")
    for i in reversed(stack[:top]): print(i)

def infixToPostfix(infix):
    ''' Convert infix expression to postfix
        TODO: Fix some usecases '''
    postfix = ""
    stack = ['(']
    operators = ("*", "+", "-", "^", "/")
    
    for symbol in infix:
        print("Symbol:", symbol, "Stack:", stack, "Postfix:", postfix)
        if symbol.isalpha(): postfix += symbol
        if symbol == '(': push(stack, symbol)
        elif symbol in operators:
            if stack[-1] in operators and postfix[-1] not in operators:
                postfix += stack[-1]
                pop(stack)
                push(stack, symbol)
            else: push(stack, symbol)
        elif symbol == ')':
            while stack[-1] in operators:
                postfix += stack[-1]
                pop(stack)
            pop(stack)

    return postfix

#print(infixToPostfix(input("Infix: ")))

def main():
    ''' Main program '''
    print("Welcome to StackTools in Python")
    run = True
    while run:
        opt = int(input("\n1) Push an element\n"+
                        "2) Pop\n"+
                        "3) Peek\n"+
                        "4) Display the stack\n\n"+
                        "Enter your option: "))

        if opt == 1:
            push(stack, int(input("Enter element: ")))
            print("Pushed the element succesfully!")
        elif opt == 2:
            res = pop(stack)
            if not res: print("Underflow error!")
            else: print("Popped element from stack succesfully!")
        elif opt == 3: print("Top:", peek(stack))
        elif opt == 4: display(stack)
        else: print("Invalid option!")

        run = not bool(input("\nHit enter to continue or anything else to exit: "))

main()
