dict = {
    'A': range(88,100),
    'B': range(80,87),
    'C':range(67,79),
    'D':range(60,66),
    'F':range(59)
}

input1 = input("Enter marks: ")

for key,value in dict.items():
    # print(key,":",value)
    input1 = int(input1)
    if input1 in value:
        print(key)
        break
    else:
        continue



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import re
RE_INT = re.compile(r'^[-+]?\d+$')
RE_INT = re.compile(r'(\.)?\d+$')
print(RE_INT.match('+0'))
print(RE_INT.match('+1.1'))
print(RE_INT.match('0.0'))
print(RE_INT.match('.000'))
print(RE_INT.match('1212'))
print(RE_INT.match('.'))
print(RE_INT.match('-.'))