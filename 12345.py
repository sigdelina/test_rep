print("classwork7")
def objects():
    line = []
def open_file():
    with open("text1.txt", encoding="utf-8") as new_file:
        lines = new_file.readlines()
        line = lines.strip("\n.,\t!?, "")
open_file()


