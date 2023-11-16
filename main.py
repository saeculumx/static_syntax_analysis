# import re
#
#
# with open('../Test-Example/userDefinedException.c', 'r') as file:
#     text = file.read()
#
# print(text)
#
# pattern = re.compile(r'\b\w*exception\w*\b', re.IGNORECASE)
#
# # Search for the pattern in the text
# matches = [(match.group(), text.count('\n', 0, match.start()) + 1) for match in pattern.finditer(text)]
#
# if matches:
#     print("Found userDefinedException:")
#     for match, line_number in matches:
#         print(f"{match} found on line {line_number}")
# else:
#     print("No userDefinedException found.")
import devided_by_0

devided_by_0.find_0()