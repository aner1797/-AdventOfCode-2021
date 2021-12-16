oxygen = []
co2 = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

def solver(binList, setting):
    index = 0
    while True:
        tmp = []
        tmpVal = 0
        for bin in binList:
            if int(bin[index]) == 0:
                tmpVal -= 1
            if int(bin[index]) == 1:
                tmpVal += 1
        
        if tmpVal >= 0:
            for bin in binList:
                if int(bin[index]) == abs(0-setting):
                    tmp.append(bin)
        else:
            for bin in binList:
                if int(bin[index]) == abs(1-setting):
                    tmp.append(bin)

        binList = tmp
        index += 1
        if len(binList) == 1:
            return binList


oxygen = solver(content_list, 1)
co2 = solver(content_list, 0)

print(int(oxygen[0], 2) * int(co2[0], 2))