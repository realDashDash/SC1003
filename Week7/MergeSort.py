
def merge_sort(list_of_items):
    list_len = len(list_of_items)

    if (list_len < 2):
        return list_of_items
    else:
        left_list = list_of_items[:list_len // 2]
        right_list = list_of_items[list_len // 2:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)

def merge(left_list, right_list):
    result_list = []

    while (left_list and right_list):
        if (left_list[0] > right_list[0]):
            result_list.append(right_list[0])
            right_list.pop(0)
        else:
            result_list.append(left_list[0])
            left_list.pop(0)

    if (left_list):
        result_list.extend(left_list)
    else:
        result_list.extend(right_list)
    
    return result_list

################## Test ##################
test_list = [1, 5, 3, 9, 7]
print(merge_sort(test_list))
