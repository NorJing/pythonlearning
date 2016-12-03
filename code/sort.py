# encoding=UTF-8

def bubble_sort(list):
    more_swaps = True
    while more_swaps:
        more_swaps = False
        for index in range(len(list) - 1):
            if list[index] > list[index + 1]: # sort from the smallest to the largest
                more_swaps = True
                list[index], list[index + 1] = list[index + 1], list[index]
    return list

# 插入排序
def insert_sort(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            list[index], list[index + 1] = list[index + 1], list[index]
            #  move everything before the index
            for before_index in range(index, 0, -1):
                if list[before_index] < list[before_index - 1]:
                    list[before_index], list[before_index - 1] = list[before_index - 1], list[before_index]
                elif list[before_index] >= list[before_index - 1]:
                    # stop this loop
                    break
    return list

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])

def quick_sort(list):
    less = []
    more = []
    pivots = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivots.append(i)

        #  得到第一组分组,继续排序分组
        less = quick_sort(less)
        more = quick_sort(more)

        return less + pivots + more

if __name__ == '__main__':
    list = [7, 1, 31, 5, 44, 2, 78, 120, 4, 1, 0]
    print(quick_sort(list))