
# Iterative Binary Search
def binary_search_iter(target, list_of_items):
    low = 0
    high = len(list_of_items) - 1

    while(low <= high):
        mid = (low + high) // 2
        if (list_of_items[mid] == target):
            return True
        elif (target > list_of_items[mid]):
            low = mid + 1
        elif (target < list_of_items[mid]):
            high = mid - 1
    else:
        return False

# Recurrsive Binary Search:
def binary_search_recur(target, list_of_items, low = 0, high = None):
    if (high == None):
        high = len(list_of_items) - 1
    
    if (low > high):
        return False
    
    mid = (high + low) // 2

    if (target == list_of_items[mid]):
        return True
    elif (target > list_of_items[mid]):
        low = mid + 1
        return binary_search_recur(target, list_of_items, low, high)
    elif (target < list_of_items[mid]):
        high = mid - 1
        return binary_search_recur(target, list_of_items, low, high)



test_list = [1, 2, 3, 4, 5, 6, 7]
print(binary_search_recur(5, test_list))