N = int(input("Enter the size of the arrays: "))
T1 = []
T2 = []
T = []
print("Enter values for array T1:")
for i in range(N):
    value = int(input(f"Element {i+1}: "))
    T1.append(value)
print("Enter values for array T2:")
for i in range(N):
    value = int(input(f"Element {i+1}: "))
    T2.append(value)
for i in range(N):
    sum_value = T1[i] + T2[i]
    T.append(sum_value)
print("The resulting array T is:")
for i in range(N):
    print(T[i])
