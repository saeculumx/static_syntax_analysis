import bisect
import re
import time


def find_functionName(l, code):
    match = ""
    start_line = 0
    names = []
    checkpoints = [0]
    pattern = re.compile(r'\bint\s+(\w+)\s*\([^)]*\)\s*{')
    # Find all matches in the C code
    matches = pattern.finditer(code)

    # Print function names and starting line numbers
    for match in matches:
        function_name = match.group(1)
        start_line_number = code.count('\n', 0, match.start()) + 1
        names.append(function_name)
        checkpoints.append(int(start_line_number))
        start_line = code.count('\n', 0, match.start()) + 1
    final = start_line + code[match.end():].count('\n') + 1
    checkpoints.append(int(final))
    index = bisect.bisect_right(checkpoints,l)
    if index == 0:
        return f"{l} not in any function"
    elif index == len(checkpoints):
        return f"{l} not in any function"
    else:
        return names[index-2]

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


start_time = time.time()
with open('../Test-Example/userDefinedRaw.c', 'r') as file:
    text = file.read()

# print(text)
lines = []
pattern = re.compile(r'\b\w*exception\w*\b', re.IGNORECASE)
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
        info = find_functionName(l, text)
        print(f"{m} found on line {l}, inside function {info}")
else:
    print("No userDefinedException found.")
print("--- %s seconds ---" % (time.time() - start_time))
