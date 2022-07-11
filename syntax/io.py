
#input
import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

#ouput
sys.stdout.write("\n".join(map(str, [])))
