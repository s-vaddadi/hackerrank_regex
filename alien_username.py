import re

n = int(input())

for _ in range(n):
    output = 'INVALID'
    line = str(input())
    match = re.match(r'^[_|.][0-9]+[A-Za-z]*[_]?$', line)
    if match is not None:
        output = 'VALID'
    else:
        output = 'INVALID'

    print(output)