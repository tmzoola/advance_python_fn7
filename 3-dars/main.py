
my_list  = [1,4,3,5]
count = 0

def quick_sort(list_a):
    global count
    length = len(list_a)
    if length<2:
        return list_a
    else:
        pivot = list_a.pop()
        left_list = []
        right_list = []
        for i in list_a:
            count = count + 1
            if pivot<i:
                right_list.append(i)
            else:
                left_list.append(i)
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(quick_sort(my_list), count)



# def insertion_sort(list_a):
#     length = len(list_a)
#     count = 0

#     for i in range(1, length):
#         while list_a[i]<list_a[i-1] and i>0:
#             count = count+1
#             list_a[i], list_a[i-1] = list_a[i-1],list_a[i]
#             i = i-1
#     return count

# print("Insertion Sort",insertion_sort(my_list1))


# def buble_sort(list_a):
#     index_length = len(list_a)-1
#     list_sorted = False
    
#     count = 0
    
#     while not list_sorted:
#         list_sorted = True
        
#         for i in range(0, index_length):
#             count = count+1
#             if list_a[i]>list_a[i+1]:
#                 list_sorted = False
#                 list_a[i], list_a[i+1] = list_a[i+1],list_a[i]
#     return count

# print("Buble sort",buble_sort(my_list2))

