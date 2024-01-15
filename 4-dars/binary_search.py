

# [1,2,3,4,5,6,7,8,9,10],  9

def binary_search(my_list, target):
    end = len(my_list)-1
    start = 0
    count = 0
    
    while start<=end:
        mid_index = (start + end)//2
        mid_value = my_list[mid_index]
        count = count+1
        
        if mid_value == target:
            return f"{target} soning list ichidagi indexsi {mid_index} va urinishlar soni {count}ta"
        elif mid_value>target:
            end = mid_index-1
        else:
            start = mid_index+1
            
    return "Bunday qiymat listda mavjud emas"


print(binary_search([2,4,8,9,11,15,78,102,111,118,221,456,789],456))
            
        
        
    
    