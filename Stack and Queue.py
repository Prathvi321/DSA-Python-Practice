class Stack:
    def __init__(self, length, initial_list=None):
        self.max_size = length
        
        try:
            if initial_list is None:
                self.list = []  
            else:
                self.list = list(initial_list)

                if len(self.list) > self.max_size:
                    raise ValueError("Initial list exceeds maximum stack length")
                    
        except Exception as e:
            print(f"Initialization Error: {e}")
            self.list = []
            self.max_size = 0  # Safe fallback assignment

    def push(self, *a):
        if len(self.list) + len(a) > self.max_size:
            print("The elements cannot be added (Overflow)")
        else:
            self.list.extend(a)
    
    def pop(self):
        if not self.list:
            print("The list is empty cannot be further popped (Underflow)")
            return None
        return self.list.pop()
        
    def display(self):
        if not self.list:
            print("Stack is empty")
        else:
            for i in reversed(self.list):
                print(i)
            print()  # Only print newline if elements were actually displayed


# Create a history stack with a maximum capacity of 5 pages
browser_history = Stack(5)

# Visit websites
browser_history.push("google.com")
browser_history.push("github.com")
browser_history.push("wikipedia.org")

print("Current active stack (Top is current page):")
browser_history.display()  # Outputs: wikipedia.org github.com google.com 

# User clicks the back button
print(f"\nClicking Back from: {browser_history.pop()}")  # Pops wikipedia.org
print("New history trace:")
browser_history.display()  # Outputs: github.com google.com



#Using Queue

class Queue:
    def __init__(self, X, initial_list=None):
        self.max_size = X

        try:
            if initial_list is None:
                self.list = []
            else:
                self.list = list(initial_list)

                if len(self.list) > self.max_size:
                    raise ValueError("Initial list exceeds maximum stack length")
                    
        except Exception as e:
            print(f"Initialization Error: {e}")
            self.list = []

    def push(self, *a):
        if not a:
            return
        try:
            if len(self.list) + len(a) > self.max_size:
                print("The new element in queue cannot be added")
            else:
                for item in reversed(a):
                    self.list.insert(0, item)
    
        except Exception as e:
            print(f"{e} occured")

    def pop(self):
        if not self.list:
            print("Queue is empty")
            return None
        return self.list.pop()
    
    def display(self):
        if not self.list:
            print("Queue is empty")
        else:
            for i in reversed(self.list):
                print(i)
            print()



# 1. Create a queue object with a maximum size of 5
my_queue = Queue(5)

# 2. Push single and multiple elements into the queue
print("--- Pushing Elements ---")
my_queue.push(10)          # Pushing a single item
my_queue.push(20, 30, 40)  # Pushing multiple items at once

# 3. Display the current state of the queue
print("--- Displaying Queue (Front to Back) ---")
my_queue.display()
# Output order will be: 10, 20, 30, 40

# 4. Try to exceed the maximum size constraint
print("--- Testing Max Size Cap ---")
my_queue.push(50, 60)      # Queue has 4 items. Adding 2 more exceeds max_size (5)
# Output: "The new element in queue cannot be added"

# 5. Pop elements from the queue (FIFO: First-In, First-Out)
print("--- Popping Elements ---")
popped_item_1 = my_queue.pop()
print(f"Popped item: {popped_item_1}")  # Output: 10 (The first item we pushed)

popped_item_2 = my_queue.pop()
print(f"Popped item: {popped_item_2}")  # Output: 20

# 6. Display the queue after popping
print("\n--- Displaying Queue After Pops ---")
my_queue.display()
# Output order will be: 30, 40

# 7. Initialize a queue with a predefined list
print("--- Initializing Queue with Existing List ---")
pre_filled_queue = Queue(5, initial_list=[100, 200, 300])
pre_filled_queue.display()

