#file = open("xyz.txt","w")
#file.write("Hello")
#print(file.seek(0))
#file.write("abc")
#file.close()

with open("xyz.txt","w") as file:
    file.write("hello")
