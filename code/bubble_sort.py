# encoding=UTF-8

def bubble_sort(list):
    more_swaps = True
    while more_swaps:
        more_swaps = False
        for index in range(len(list) - 1):
            if list[index] > list[index + 1]: # sort from the smallest to the largest
                more_swaps = True
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp

    return list

# 插入排序
def insert_sort(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            temp = list[index]
            list[index] = list[index + 1]
            list[index + 1] = temp
            #  move everything before the index
            for before_index in range(index, 0, -1):
                if list[before_index] < list[before_index - 1]:
                    temp1 = list[before_index]
                    list[before_index] = list[before_index - 1]
                    list[before_index - 1] = temp1
                elif list[before_index] >= list[before_index - 1]:
                    # stop this loop
                    break

    return list

if __name__ == '__main__':
    list = [1,31,5,44,2,78,120,4,1,0]
    print(insert_sort(list))
#    print(bubble_sort(list))
