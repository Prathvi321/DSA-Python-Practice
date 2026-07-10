def clean(name):
    left = 0
    for right in range(1, len(name)):
        print(f"{name[left]}  {name[right]}")
        if name[left] != name[right]:
            left += 1
            name[left] = name[right]
    return left + 1

name = ["Aman", "Aman", "Aman", "Bhavana", "Chirag", "Chirag", "Chirag", "Diya"]

count = clean(name)
print(name[:count])


#Bug fixed for unsorted array

def clean_unsorted(name):
    seen = set()  # Tracks names we already encountered
    left = 0      # Tracks where to write the next unique name
    
    for right in range(len(name)):
        if name[right] not in seen:
            seen.add(name[right])      # Remember this name
            name[left] = name[right]   # Overwrite at the left pointer
            left += 1                  # Move left pointer forward
            
    return left  # Returns total number of unique elements

name = ["Aman", "Aman", "Aman", "Aman", "Bhavana", "Chirag", "Chirag", "Aman", "Chirag", "Diya"]
count = clean_unsorted(name)

print(f"Unique count: {count}")
print(name[:count])  # Slice to see only the valid unique elements

