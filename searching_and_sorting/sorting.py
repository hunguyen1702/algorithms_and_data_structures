#def bubbleSort(alist):
#    for passnum in range(len(alist)-1,0,-1):
#        for i in range(passnum):
#            if alist[i]>alist[i+1]:
#                temp = alist[i]
#                alist[i] = alist[i+1]
#                alist[i+1] = temp
#
#
#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)
#
#
#def shortBubbleSort(alist):
#    exchanges = True
#    passnum = len(alist)-1
#    while passnum > 0 and exchanges:
#       exchanges = False
#       for i in range(passnum):
#           if alist[i]>alist[i+1]:
#               exchanges = True
#               temp = alist[i]
#               alist[i] = alist[i+1]
#               alist[i+1] = temp
#       passnum = passnum-1
#
#
#alist=[20,30,40,90,50,60,70,80,100,110]
#shortBubbleSort(alist)
#print(alist)


#def selectionSort(alist):
#    for i in range(len(alist) - 1):
#        idx = i
#        for j in range(i + 1, len(alist)):
#            if alist[idx] > alist[j]:
#                idx = j
#        alist[i], alist[idx] = alist[idx], alist[i]
#
#
#alist = [54,26,93,17,77,31,44,55,20]
#selectionSort(alist)
#print(alist)


#def insertionSort(alist):
#   for index in range(1,len(alist)):
#
#     currentvalue = alist[index]
#     position = index
#
#     while position>0 and alist[position-1]>currentvalue:
#         alist[position]=alist[position-1]
#         position = position-1
#
#     alist[position]=currentvalue
#
#
#alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)


#def mergeSort(alist):
#    print("Splitting ",alist)
#    if len(alist)>1:
#        mid = len(alist)//2
#        lefthalf = alist[:mid]
#        righthalf = alist[mid:]
#
#        mergeSort(lefthalf)
#        mergeSort(righthalf)
#
#        i=0
#        j=0
#        k=0
#        while i < len(lefthalf) and j < len(righthalf):
#            if lefthalf[i] < righthalf[j]:
#                alist[k]=lefthalf[i]
#                i=i+1
#            else:
#                alist[k]=righthalf[j]
#                j=j+1
#            k=k+1
#
#        while i < len(lefthalf):
#            alist[k]=lefthalf[i]
#            i=i+1
#            k=k+1
#
#        while j < len(righthalf):
#            alist[k]=righthalf[j]
#            j=j+1
#            k=k+1
#    print("Merging ",alist)
#
#
#alist = [54,26,93,17,77,31,44,55,20]
#mergeSort(alist)
#print(alist)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

