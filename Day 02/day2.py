horizontal = 0
depth = 0

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for item in content_list:
    x, nr = item.split()
    if x == "forward":
        horizontal += int(nr)
    if x == "up":
        depth -= int(nr)
    if x == "down":
        depth += int(nr)

print(depth*horizontal)