def quick_sort(list):
    if len(list) <= 1:
        return list

    else:
        pivot = list[0]
        lesser = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)



print(quick_sort([])) 
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))