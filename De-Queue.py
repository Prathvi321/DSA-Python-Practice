#Double Ended Queue

class de_queue:
    def __init__(self, X, initial_list = None):
        self.maxsize = X

        try:
            if initial_list is None:
                self.list = []
            else:
                self.list = list(initial_list)

                if len(self.list) > self.maxsize:
                    raise ValueError("Initial list exceeds maximum queue length")
        
        except Exception as e:
            print(f"Initialization error : {e}")
            self.list = []

    def front_push(self, *a):
        if len(self.list) + len(a) > self.maxsize:
            print("Items cannot be added")
        else:
            for item in reversed(a):
                self.list.insert(0, item)

    def back_push(self, *a):
        if len(self.list) + len(a) > self.maxsize:
            print("Items cannot be added")
        else:
            self.list.extend(a)

    def front_pop(self):
        if not self.list:
            print("Queue is Empty")
        else:
            self.list.pop(0)
        
    def back_pop(self):
        if not self.list:
            print("Queue is Empty")
        else:
            self.list.pop()

    def display(self, reverse=False):
        if not self.list:
            print("Queue is empty")
        else:
            items_to_print = reversed(self.list) if reverse else self.list
            
            for item in items_to_print:
                print(item)

# 1. Create a queue object with a max size of 5
my_queue = de_queue(5, [10, 20])

# 2. Add elements to the front and back
print("--- Adding Elements ---")
my_queue.back_push(30, 40)
my_queue.front_push(5)

# 3. Display the current queue states
print("\n--- Standard Display (Front to Back) ---")
my_queue.display()

print("\n--- Reversed Display (Back to Front) ---")
my_queue.display(reverse=True)

# 4. Try to overflow the queue (Max size is 5, currently has 5)
print("\n--- Testing Overflow Check ---")
my_queue.back_push(50)

# 5. Remove elements from both ends
print("\n--- Removing Elements ---")
my_queue.front_pop()
my_queue.back_pop()

print("\n--- Display After Popping ---")
my_queue.display()


# Another De-Queue efficient program

from collections import deque
queue = deque()

queue.append("Ravi")
queue.append("Priya")
queue.append("You")
queue.append("Karan")

print(queue)

first = queue.popleft()
print(queue)

last = queue.pop()

print(queue)

