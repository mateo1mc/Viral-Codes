import string
import time

text = "Hello World!"
temp = ''
for ch in text:
    for i in string.printable:
        if i == ch or ch == i:
            time.sleep(0.02)
            print(temp+i)
            temp+=ch
        else:
            time.sleep(0.02)
            print(temp+i)
