def dvr():
    global dist, temp, n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    temp[i][j] = k

    for i in range(n):
        print(f"\n\nState value for router {i + 1} is:")
        for j in range(n):
            print(f"\tnode {j + 1} via {temp[i][j] + 1} Distance {dist[i][j]}")
    print("\n")


# Input section
n = int(input("Enter the number of nodes: "))

dist = []
temp = [[0] * n for _ in range(n)]

print("\nEnter the distance matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if i == j:
            row[j] = 0
    dist.append(row)
    temp[i] = list(range(n))

# Perform DVR algorithm
dvr()

# Update section
i = int(input("Enter the value of i: ")) - 1
j = int(input("Enter the value of j: ")) - 1
x = int(input("Enter the new cost: "))

dist[i][j] = x
print("After update\n\n")
dvr()
