from pathlib import Path

# 1. READING FROM A FILE

#path = Path('/Users/buhlemtshali/Desktop/Python-Full-Stack/full-stack-python/day-11-file-handling/pi_digits.txt')

path = Path("example.txt")

path.write_text("example file")

print(path)