import re

my_str = """
myVariableIsHere = 17
anotherVariable = "someString"
boolVariable = True
"""

new_str = re.sub(r'([A-Z])', lambda match: "_" + match.group(1).lower(), my_str)

print(new_str)