classroom = [[85,60,78], [72,88,91], [95,60,83]]
for i in classroom:
    for j in i:
        print(j, end = " ")
    print("\n-- -- --")

#Two Pointer Technique


def Find_Two_Number(List, X):
    Left = 0
    Right = len(List) - 1
    all_pairs = []
    List.sort()
    
    while Left < Right:
        Sum = List[Left] + List[Right]
        if Sum == X:
            all_pairs.append([List[Left], List[Right]])
            Left += 1
            Right -= 1
        elif Sum < X:
            Left += 1
        else:
            Right -= 1
            
    return all_pairs

List = [1, 3, 4, 5, 6, 8, 11]
X = int(input("Enter the targeted number : "))
print(Find_Two_Number(List, X))


#Same direction technique


