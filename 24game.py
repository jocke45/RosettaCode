import random
import sys

def a(a, b):
    return float(a) + float(b)

def d(a, b):
    return float(a) / float(b)
def m(a, b):
    return float(a) * float(b)
def s(a, b):
    return float(a) - float(b)

def check_inp(num, inp):
    i=1
    if len(inp) < 7:
        print("too short input, exiting")
        sys.exit()
    while i < 7:
        print(num.find(inp[i]))
        i += 2

numbers = [random.randint(1,9) for i in range(0,4)]
print(numbers)

inp = input()


result = inp[0]
check_inp(numbers, inp)

ind = 1
while ind < 7:
    if inp[ind] == '+':
        result = a(result, inp[ind+1])
    if inp[ind] == '/':
        result = d(result, inp[ind+1])
    if inp[ind] == '*':
        result = m(result, inp[ind+1])
    if inp[ind] == '-':
        result = s(result, inp[ind+1])
    ind += 2
print(result)