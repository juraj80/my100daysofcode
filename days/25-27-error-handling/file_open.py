import sys
file_name = sys.argv[1]
text = []

try:
    fh = open(file_name,'r')
except IOError:
    print(f'No such file or directory: "{file_name}"')
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[:100])
