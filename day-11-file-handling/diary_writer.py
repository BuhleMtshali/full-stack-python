from pathlib import Path

path = Path('/Users/buhlemtshali/Desktop/Python-Full-Stack/full-stack-python/day-11-file-handling/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)