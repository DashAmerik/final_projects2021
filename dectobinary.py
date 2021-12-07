dec = int(input())
L = []

def convert(n):
    while n > 0:
        L.append(str(n%2))
        n = n//2
    L.reverse()
    s = ''.join(L)
    return s

print(convert(dec))
