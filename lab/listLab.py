import random
from collections import Counter


def sortList(list):
    # descending
    list.sort(reverse=True)
    return list


def countTargetInList(list, target):
    counter = Counter(list)
    count = counter[target]
    return count


def getTargetIndexInList(list, target):
    # [index for index, element in enumerate(list) if smallest == element]
    indexs = []
    for index, element in enumerate(list):
        if element == target:
            indexs.append(index)
    return indexs


if __name__ == '__main__':
    list = [10,10,18,19,37,10,28,33]

    print("List:", list)

    # descending
    list.sort(reverse=True)
    print("Sorted List:", list)

    print("Maximum:", max(list))
    
    print("Smallest:", min(list))

    print("Index for 37:", list.index(37))

    print("RandomChoice:", random.choice(list))

    print("Index for 10::", getTargetIndexInList(list, 10))
    
    print("Count Number of 10::", countTargetInList(list,10))