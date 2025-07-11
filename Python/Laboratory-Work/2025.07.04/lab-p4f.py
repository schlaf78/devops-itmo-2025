import os

folder = os.getcwd()
asw = set()
search = input("Enter any text: ")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as fp:
                for line in fp:
                    if search in line:
                        asw.add((line.strip(), filepath))
        except Exception:
            continue

for line, path in asw:
    print(f"{line}\n[Found in: {path}]\n")

#2 Get file info
with open("file.txt", "r") as parsingfile:
    filecontent = parsingfile.read()

letterscount = sum(map(str.isalpha, filecontent))
wordscount = len(filecontent.split())
linescount = filecontent.count("\n") + (1 if filecontent else 0)
print(f"""File contains:
      {letterscount} letters
      {wordscount} words
      {linescount} lines""")

#3 Pathlib module
