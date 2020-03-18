import os

path = os.getcwd()

with open(path + ".\b_file\a.txt", "r") as file:
import os
path = os.getcwd()
a_path = os.path.join(path, "b_file/a.txt")
print(a_path)


os.path.abspath(os.path.join(path, ".."))