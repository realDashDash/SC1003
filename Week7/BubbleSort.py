
def swap(a, b):
    return b, a

# an less efficient way
def bubble_sort_simple(alist):
    for i in range(len(alist) - 1):
        if (alist[i] > alist[i+1]):
            alist[i], alist[i+1] = swap(alist[i], alist[i+1])
        else:
            pass
    return alist

def bubble_sort_imporved(alist):
    for passnum in range(len(alist)):
        swapped = False
        for i in range(len(alist) - passnum - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = swap(alist[i], alist[i+1])
                swapped = True
        print("Pass", passnum+1, ": ", alist)
        if (not swapped):
            break

testList = [1, 5, 3, 9, 7]
testList = [1, 3, 5, 7, 9]
print(bubble_sort_imporved(testList))