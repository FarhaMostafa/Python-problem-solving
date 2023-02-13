global_list=[1,2,3]

def add_to(item):  #not pure function       {pure function: no efect beyond its own scope}
    return global_list.append(item)

add_to(4)
print(global_list)    


#pure function
def add_to_lest(lest,item):
    n=lest.copy()
    n.append(item)
    return n

print(add_to_lest(global_list,6))    
print(global_list)