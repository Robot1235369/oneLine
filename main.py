file_name = input("file path: ")

file = open(file_name, "r")
lines = file.readlines()
file.close()

code = ""

for line in range(len(lines)):
    lines[line] = lines[line].strip()
    for char in range(len(lines[line])):
        try:
            if lines[line][char] == "/":
                if lines[line][char + 1] == "/":
                    lines[line] = lines[line][0:char]
            elif lines[line][char] == "@":
                if lines[line][char + 1] == "O":
                    if lines[line][char + 2] == "v":
                        if lines[line][char + 3] == "e":
                            if lines[line][char + 4] == "r":
                                if lines[line][char + 5] == "r":
                                    if lines[line][char + 6] == "i":
                                        if lines[line][char + 7] == "d":
                                            if lines[line][char + 8] == "e":
                                                lines[line] += " "
        except IndexError:
            pass
    code += lines[line]

file = open(file_name, "w")
file.write(code)
file.close()