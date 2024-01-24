def merge_sort(my_list):
    
    if len(my_list)>1:
        mid = len(my_list)//2
        left_list = my_list[:mid]
        right_list = my_list[mid:]
        
        merge_sort(left_list)
        merge_sort(right_list)
        
        i=j=k=0
        
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                my_list[k] = left_list[i]
                i+=1
            else:
                my_list[k] = right_list[j]
                j+=1
            k+=1
        
        while i<len(left_list):
            my_list[k]=left_list[i]
            i+=1
            k+=1
        
        while j<len(right_list):
            my_list[k]= right_list[j]
            j+=1
            k+=1
            
my_list = [38,9,8,7,3,9494,49899,4359,985,986,9965,652,9]

merge_sort(my_list)

print(my_list)
        