from pathlib import Path
import random

PROJ_DIR = Path(__file__).parent
# Using this variable allows us to easily change the file we want to read from
readFrom = "names.txt"
writeTo = "persons3.txt"

r = open(PROJ_DIR / readFrom, "r")
w = open(PROJ_DIR / writeTo, "w")

# r is a large file with 4k+ names, 
# choose randomly from it X times and write it plus a random int from 10-80
# separated by ,

numEntries = 1000

lines = r.readlines()
for i in range(numEntries):
    line = random.choice(lines).strip()
    w.write(f"{line}, {random.randint(10,80)}\n")

r.close()
w.close()