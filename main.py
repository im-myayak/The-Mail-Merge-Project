
PLACEHOLDER = "[name]"

with open("invited_names.txt") as file:
    names = file.readlines()
with open("starting_letter.txt") as file1:
    letter = file1.read()
    for name in names:
        name = name.strip()
        with open(f"letter_for_{name}", mode='w') as file:
            file.write(letter.replace(PLACEHOLDER, name))

