"""
    QUEUES
"""

# Initialize an empty queue as a python list
q = []
front = rear = None

def enqueue(q, element):
    ''' Enqueue an element into the queue '''
    global front, rear
    q.append(element)
    front = 0
    rear = len(q) - 1
    print("Element", element, "enqueued in queue succesfully!")

def dequeue(q):
    ''' Dequeue - remove the front element in the queue '''
    global front, rear
    if rear is None:
        print("Underflow error!")
        return False

    q.pop(front)
    print("Dequeued first (front) element succesfully!")
    if q == []: front = rear = None
    else: return q[front]

def peek(q):
    ''' Peek - display the front and rear element of the queue '''
    global front, rear
    if rear is None:
        print("Underflow error!")
        return

    print("Front:", q[front])
    print("Rear:", q[rear])

def display(stack):
    ''' Display the contents of the queue '''
    global front, rear
    if rear is None:
        print("Underflow error!")
        return
    
    print(stack[front], "<- front")
    for i in reversed(stack[front+1:rear]): print(i)
    print(stack[rear], "<- rear")

def main():
    ''' Main program '''
    print("Welcome to QueueTools in Python")
    run = True
    while run:
        opt = int(input("\n1) Enqueue an element\n"+
                        "2) Dequeue\n"+
                        "3) Peek\n"+
                        "4) Display the stack\n\n"+
                        "Enter your option: "))

        if opt == 1: enqueue(q, int(input("Enter element: ")))
        elif opt == 2: dequeue(q)
        elif opt == 3: peek(q)
        elif opt == 4: display(q)
        else: print("Invalid option!")

        run = not bool(input("\nHit enter to continue or anything else to exit: "))

main()
