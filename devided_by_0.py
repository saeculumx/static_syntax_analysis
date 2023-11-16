import re

array = []
functionRangeList = []


def read():
    with open('../Test-Example/div.c', 'r') as file:
        text = file.read()
    # print(text)
    return text


def find():
    code = read()
    pattern = re.compile(r'{|}')
    matches = [(match.group(), match.start(), match.end()) for match in pattern.finditer(code)]
    brace_pairs = [(brace, st, en) for brace, st, en in matches if brace in {'{', '}'}]

    for brace, st, en in brace_pairs:
        array.append(st)
        print(f"Found '{brace}' at line {st,en}")

    pair_process = array.copy()
    length = len(array)
    for i in range(round(length / 2)):
        pair = pair_process[:2]
        pair_process = pair_process[2:]
        functionRangeList.append(pair)
    print(functionRangeList)
    return (functionRangeList)


def find_0():
    find()
    code = read()
    #print(code)
    for f in functionRangeList:
        start = f[0]
        end = f[1]
        selected_lines = code[start+1:end]
        print(selected_lines)
