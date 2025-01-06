import os
from os import write

file_name = "pramod.txt"
content = "This is a Pramod's File ABC"

with open(file_name,"w") as file1:

    file1.write(content)
    file1.read()

with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)


# os.chdir("Desktop")

def shiva():
    print("Main method")

if __name__ == "__main__":
    shiva()

#if __name__ == "__main__": #Python Int -> Main methos is -> Line Main
    #main()