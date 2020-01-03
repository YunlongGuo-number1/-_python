def bubbleSort(alist):  #o(n**2)
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if int(alist[i]) > int(alist[i+1]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def selectSort(alist):  #o(n**2)
    for fillslot in range(len(alist)-1, 0, -1):
        postionOfmax = 0
        for location in range(1, fillslot):
            if int(alist[location]) > int(alist[postionOfmax]):
                postionOfmax = location
        alist[fillslot], alist[postionOfmax] = alist[postionOfmax], alist[fillslot]
    return alist

def insertSort(alist):  #o(n**2)
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        postion = index

        while postion > 0 and int(alist[postion-1]) > int(currentvalue):
            alist[postion] = alist[postion-1]
            postion = postion -1

        alist[postion] = currentvalue

    return alist

def shellSort(alist):   #o(n)~o(n**2)
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for stratpostion in range(sublistcount):
            gapInsertSort(alist, stratpostion, sublistcount)
            sublistcount = sublistcount // 2

    return alist
def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        postion = i

        while postion >= gap and int(alist[postion-gap]) > int(currentvalue):
            alist[postion] = alist[postion - gap]
            postion = postion - gap

        alist[postion] = currentvalue

def mergeSort(alist):   #o(nlogn)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if int(lefthalf[i]) < int(righthalf[j]):
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    return alist

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    return alist

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = parttion(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def parttion(alist, first, last):
    basevalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and int(alist[leftmark]) <= int(basevalue):
            leftmark = leftmark + 1
        while leftmark <= rightmark and int(alist[rightmark]) >= int(basevalue):
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark

n = int(input())
a = input()
array = a.split( )
array = quickSort(array)
#array = mergeSort(array)
#array = shellSort(array)
#array = insertSort(array)
#array = bubbleSort(array)
#array = selectSort(array)
for j in array:
    print(j, end=" ")
