class StackManager:
    def __init__(self, *args):
        try:
            self.L = list(args)
        except Exception as e:
            print(f"Initialization Error: Could not convert input to list. {e}")
            self.L = []
    
    def push(self, a):
        try:
            self.L.append(a)
        except Exception as e:
            print(f"Push Error: Failed to add item {a}. {e}")
        return self.L

    def pop(self):
        try:
            if not self.L:
                raise IndexError("Cannot pop from an empty stack.")
            self.L.pop()
        except IndexError as ie:
            print(f"Pop Error: {ie}")
        except Exception as e:
            print(f"Unexpected Pop Error: {e}")
        return self.L

    def display(self):
        try:
            if not self.L:
                print("Stack is empty, nothing to display.")
                return
            for item in self.L:
                print(item, end=" ")
        except Exception as e:
            print(f"Display Error: Failed to print contents. {e}")
        finally:
            print()
            print("- " * len(self.L))

List_1 = StackManager(1,2,3,4,5,6,7,8,9,10)
List_2 = StackManager(2,4,6,8,10,12,14,16,18,20)

List_1.display()
List_2.pop()
List_2.push(19)
List_2.display()