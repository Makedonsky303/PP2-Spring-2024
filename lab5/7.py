import re

my_str = """
my_variable_is_here = 17
another_variable = "some_string"
bool_variable = True
"""

new_str = re.sub(r'(?:_)([a-z])', lambda match: match.group(1).upper(), my_str)

print(new_str)