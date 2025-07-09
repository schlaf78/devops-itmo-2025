import os

#print(os.getcwd())
#os.mkdir('demo_dir')
#os.listdir(path=".")
Folder = os.getcwd()
Asw = set()
Search = input ("Enter any text:")

for filename in os.listdir(Folder):
    Filepath = os.path.join(Folder, filename)
    print(Filepath)

