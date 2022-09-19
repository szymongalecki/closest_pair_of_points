import matplotlib.pyplot as plt

"""
run:
cat rd100-tsp.txt | python3 cp.py
cat eil101-tsp.txt | python3 cp.py
"""

# point coordinates are held in the list of tuples
points = []
i = input()

# obtain point coordinates
while i != "":
    if i[0].isalpha():
        pass
    else:
        try:
            id, x, y = [float(_) for _ in i.split()]
            points.append((x, y))
        except ValueError:
            pass
    try:
        i = input().strip()
    except EOFError:
        break

# find closest points
min_d = float("inf")
min_points = []

# quadratic solution
for p1 in points:
    for p2 in points:
        if p1 != p2:
            d = ((abs(p1[0] - p2[0])) ** 2 + (abs(p1[1] - p2[1])) ** 2) ** (1 / 2)
            if d < min_d:
                min_d = d
                min_points = [p1, p2]

# left and right point
if min_points[0][0] <= min_points[1][0]:
    l, r = min_points[0], min_points[1]
else:
    l, r = min_points[1], min_points[0]

# plot the result
plt.style.use("grayscale")
fig, ax = plt.subplots()
fig.suptitle("Closest points", fontsize=16)
ax.set_title(f"{l} - {r}", fontsize=12)
for p in points:
    ax.scatter(p[0], p[1])
ax.plot(
    [min_points[0][0], min_points[1][0]],
    [min_points[0][1], min_points[1][1]],
    "bo",
    linestyle="--",
)
plt.show()
