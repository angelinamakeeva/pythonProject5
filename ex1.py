with open("input.txt", "r") as file:
    text = file.read()
text = text.upper()
with open("output.txt", "w") as file:
    file.write(text)