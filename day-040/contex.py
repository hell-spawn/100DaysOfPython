"""
Context manager files
"""


import csv
from pathlib import Path

some_source = [[2,3,5], [7,11,13], [17,19,23]]
target_path  = Path.cwd()/"data"/"test.csv"

# When we use a file as a context manager, the file is automatically closed at the end
# of the indented context block.

with target_path.open('w', newline='') as target_file:
    writer = csv.writer(target_file) 
    writer.writerow(['column', 'data','heading'])
    writer.writerows(some_source)

print(f'Finished writing {target_path.name}')

try:
    with target_path.open('w', newline='') as target_file:
        writer = csv.writer(target_file)
        writer.writerow(['column', 'data','heading'])
        writer.writerow(some_source[0])
        raise Exception("Testing close resources")
except Exception as e:
    print(f'{target_file.closed}')
    print(f'{e}')

