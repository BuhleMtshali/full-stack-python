from pathlib import Path

# 1. READING FROM A FILE

path = Path('/Users/buhlemtshali/Desktop/Python-Full-Stack/full-stack-python/day-11-file-handling/pi_digits.txt')

file_contents = path.read_text()

print(f"Read Example: {file_contents}")
