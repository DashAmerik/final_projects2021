signnum = input()
num = int(signnum[1])
L = []
A = [[0]*(num+1) for i in range(num+1)]

def sign(sign1,n1,n2):
    sign = sign1[0]
    if sign == '+':
        return(n1+n2)
    if sign == '-':
        return(n1-n2)
    if sign == '*':
        return(n1*n2)
    if sign == '/':
        return(n1/n2)


for i in range(int(num)+1):
    for j in range(int(num)+1):
        A[i][j] = sign(signnum, j, i)

for i in A:
    print(i)
