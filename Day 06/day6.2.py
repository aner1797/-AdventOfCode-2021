my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split(",")

family = {}
for age in range(9): family[age]= sum(int(x)==age for x in content_list)

def day(family):
    baby = family[0]
    for i in range(0,8):
        family[i] = family[i+1]
        if i == 6:
            family[i] += baby
    
    family[8] = baby
    return family


for i in range(0,256):
    family = day(family)
print(sum(family.values()))