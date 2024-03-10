import re

n = int(input())

for _ in range(n):
    output = 'INVALID'
    line = str(input())
    match = re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', line)
    if match is not None:
        output = 'YES'
    else:
        output = 'NO'

    print(output)