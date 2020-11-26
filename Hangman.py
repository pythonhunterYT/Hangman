import random

def func(ls1, ls2, x):
    idx = ls1.index(x)
    ls2[idx] = x
    
words = ["code", "computer", "python", "mac", "linux"]
sel = random.choice(words)
ls = list(sel)
ls0 = []
count = 10
base = 0
sel_len = int(len(sel))
for i in range(sel_len):
    ls0.append('x')
while True:
    print(ls0)
    if base == sel_len:
        print('You won')
        break
    elif count == 0:
        print('you lost')
        break
    try1 = input('Enter the letters: ')
    if try1 in ls:
        print('Correct!')
        func(ls, ls0, try1)
        base += 1
    else:
        print('Wrong!')
        count -= 1
