import matplotlib.pyplot as plt

# point coordinates are held in the list of tuples for now
points = []
i = input()

# obtain and print point coordinates
while i != "":
    if i == "EOF":
        break
    elif i[0].isalpha():
        pass
    else:
        id, x, y = [float(_) for _ in i.split()]
        points.append((x, y))
    i = input().strip()
print(points)

# plot points
fig, ax = plt.subplots()
for p in points:
    ax.scatter(p[0], p[1])
plt.show()
