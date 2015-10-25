#-*-coding:utf-8-*-
#quick sort[百度百科](http://baike.baidu.com/link?url=cSEMQ7iluCzQiJuctz_wZudKQIlKo9r2P0qOaPo2Pqg7ooz91-OdlXI6_Alifiee5mpYvnivUMTNf4KOJipvS1LmsO7PDq7VbdtHeviZlXRMvDTPIxHFVy1dkT412leuTV4ncKHFiKnlTjj8RhCrRAU0Wlhq3QNgd9czUDZ6Fh2G7BQNJODcVsUzeesJx2LP)
#[JS算法演示](http://graph.jm47.com/example/sort.html)
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

#print quickSort([2,5,4,1,3,6],0,5)


def q(L,left,right):
    i = left
    j = right

    if(i>=j):
        return L
    key = L[i]
    while i<j:
        while i<j and L[j]>=key:
            j = j-1
        L[i] = L[j]
        while i<j and L[i]<=key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    q(L,left,i-1)
    q(L,j+1,right)

    return L

#print q([2,5,4,1,3,6],0,5)

def q1(L,left,right):
    i = left
    j = right

    if(i>=j):
        return L
    key = L[i]
    while i<j:
        while i<j and L[j]>=key:
            j = j-1
        L[i] = L[j]
        while i<j and L[i]<=key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    q1(L,left,i-1)
    q1(L,j+1,right)
    return L

print q1([2,5,4,1,3,6],0,5)

