'''
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

number = 6
print("the factorial of 3 = ", factorial(number))
'''

L = [3,7,1,8,3,6,6,2,3,8,5,1,2,4,8,2]

def split(myList):
    if len(myList)<=1:
        return myList

    left = split(myList[:int(len(myList)/2)])
    right = split(myList[int(len(myList)/2):])

    return merge(left,right)


def merge(left,right):
    finalList = []
    leftc = 0
    rightc = 0
    while leftc < len(left) and rightc < len(right):
        if left[leftc] < right[rightc]:
            finalList.append(left[leftc])
            leftc += 1
        else:
            finalList.append(right[rightc])
            rightc += 1
    finalList.extend(left[leftc:])
    finalList.extend(right[rightc:])
    return finalList

print(split(L))
