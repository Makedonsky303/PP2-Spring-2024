f = open("some_file.txt")
content = f.read()
f.close()

duplicate = open("duplicate.txt","w")
duplicate.write(content)
duplicate.close()