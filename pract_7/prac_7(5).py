
filename = "triangle.txt"

rows = 5
triangle_pattern = ""
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    triangle_pattern += spaces + stars + "\n"


with open(filename, "w") as file:
    file.write(triangle_pattern)

print("Triangle pattern saved to", filename)
