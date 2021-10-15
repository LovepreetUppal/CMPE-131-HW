def swap_last_item(list):
    #Removes the first number 
    first = list.pop(0) 
    #Remove the last number
    last = list.pop(-1)
    #Insert the last number in position 0(front)
    list.insert(0, last) 
    list.append(first)  
     
    return list
