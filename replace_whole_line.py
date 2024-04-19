import os
import re

file = 'lfn_ulimit_makeup'

with open(file, 'r') as f:
    content = f.readlines()

lfn = 'TOP_0001'
pattern = rf'{lfn}\,.*\n'

for i, line in enumerate(content):
    if re.search(pattern, line):
        content[i] = re.sub(pattern, f'{lfn}, M=999', line)

with open(file, 'w') as f:
    f.writelines(content)

for line in content:
    print(line.strip())
