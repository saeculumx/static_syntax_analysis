import re


def pure_literal_check(text, lines):
    pattern = re.compile(r'\("([^"]*exception[^"]*)"\)', re.IGNORECASE)
    ms = [(match.group(), text.count('\n', 0, match.start()) + 1) for match in pattern.finditer(text)]
    for m, l in ms:
        if line_number == l:
            print(f"{m} at line {l} is pure literal")
            lines.remove(lines[len(lines) - 1])
    define_check(text, lines)


def define_check(text, lines):
    pattern = re.compile(r'\bvoid\s+(\w+)\s*\([^)]*\)\s*', re.IGNORECASE)
    ms = [(match.group(), text.count('\n', 0, match.start()) + 1) for match in pattern.finditer(text)]
    for m, l in ms:
        if line_number == l:
            print(f"{m} at line {l} is function defining")
            lines.remove(lines[len(lines) - 1])
    comment_check(text, lines)


def comment_check(text, lines):
    pattern = re.compile(r'(/\*([^*]|(\*+[^*/]))*\*+/|//.*)', re.IGNORECASE)
    ms = [(match.group(), text.count('\n', 0, match.start()) + 1) for match in pattern.finditer(text)]
    for m, l in ms:
        if line_number == l:
            print(f"{m} at line {l} is comment")
            lines.remove(lines[len(lines) - 1])


with open('../Test-Example/userDefinedException.c', 'r') as file:
    text = file.read()

# print(text)
lines = []
pattern = re.compile(r'\b\w*exception\w*\b', re.IGNORECASE)
# Search for the pattern in the text
matches = [(match.group(), text.count('\n', 0, match.start()) + 1) for match in pattern.finditer(text)]

if matches:
    print("Matching starting")
    for match, line_number in matches:
        lines.append([match, line_number])
        # Pure literal check
        pure_literal_check(text, lines)

        # Define check
    print("Real Exception are listed below: ")
    for m, l in lines:
        print(f"{m} found on line {l}")
else:
    print("No userDefinedException found.")

# import devided_by_0
#
# devided_by_0.find_0()
