from os import listdir

dirs = []
files = []
path = ""
i = 0

contents = listdir()

try:
    while True:
        for content in contents:
            print(content)
            if "." not in content:
                dirs.append(path + content + "/")
            elif ".java" in content:
                files.append(path + content)
        print(dirs)
        path = dirs[i]
        contents = listdir(path)
        i += 1
except():
    pass

print(dirs)
print(file)