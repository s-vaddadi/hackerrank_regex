import re

n = int(input())

for _ in range(n):
    line = str(input())
    match = re.match(r'^([0-9]{1,3})[-| ]([0-9]{1,3})[-| ]([0-9]{4,10})$', line)
    if match is not None:
        CountryCode, LocalAreaCode, Number = match.groups()
        print(f"CountryCode={CountryCode},LocalAreaCode={LocalAreaCode},Number={Number}")