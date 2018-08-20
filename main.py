import sys

# The source file is the 1st argument to the script
if len(sys.argv) != 2:
    print('usage: %s <conexiones.dsl>' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        print(parts) 
