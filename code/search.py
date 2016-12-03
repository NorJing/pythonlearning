# -*- coding: utf-8 -*-

# 二分查找
def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item == list[mid]:
            print("Found %d" % item)
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

def sequencial_search(list, item):
    pos = 0
    found = False
    while pos < len(list) and not found:
        if item == list[pos]:
            print("Found %d" % item)
            found = True
        else:
            pos = pos + 1

    return found

test = [1,3,5,7,9,12,15,22,54]
# print(binary_search(test, 12))
# print(binary_search(test, 2))

test1=[1,3,2,56,21,90,2,22]
print(sequencial_search(test1, 22))
print(sequencial_search(test1, 10))
print(sequencial_search(test1, 2))
