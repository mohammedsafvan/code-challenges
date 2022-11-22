'''
Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.
'''

# def most_frequent_item_count(collection):
def most_frequent_item_count(collection):
    dic = {}
    if len(collection) == 0:
        return 0
    else:
        for i in collection:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic.get(i) + 1
    return max(dic.values())

print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))        