from re import L
import matplotlib.pyplot as plt
import sys

"""
run:
cat rd100-tsp.txt | python3 cp.py
cat eil101-tsp.txt | python3 cp.py
"""

# point coordinates are held in the list of tuples
points = []

# read using the passed function
def read(i, func):
    while i != "":
        # try to obtaining coordinates
        try:
            _, x, y = i.split()
            points.append((float(x), float(y)))
        except ValueError:
            pass
        # try obtaining the next line of input
        try:
            i = func()
        except EOFError:
            break


# STDIN or file
if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as reader:
        i = reader.readline()
        read(i, reader.readline)
else:
    i = input()
    read(i, input)


print(points)

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

# plot the result
plt.style.use("grayscale")
fig, ax = plt.subplots()
fig.suptitle("Closest points", fontsize=16)
ax.set_title(f"{min(min_points)} - {max(min_points)} = {min_d}", fontsize=12)
for p in points:
    ax.scatter(p[0], p[1])
ax.plot(
    [min_points[0][0], min_points[1][0]],
    [min_points[0][1], min_points[1][1]],
    "bo",
    linestyle="--",
)
plt.show()
