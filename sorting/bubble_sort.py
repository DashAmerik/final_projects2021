'''
task = 23573268312

1:23532673128
2:23325631278

x,y = 5,6

'''

def bubble_sort(myList):
    for a in range(0,len(myList)-1):
        for i in range(0,len(myList)-1):
            if myList[i] > myList[i+1]:
                myList[i],myList[i+1] = myList[i+1],myList[i]
    return myList



ls = [2,3,5,7,3,2,6,8,3,1,2]
print(bubble_sort(ls))
