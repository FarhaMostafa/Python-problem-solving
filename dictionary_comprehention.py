using_range={x:x *2 for x in range(12)}
print("using range ")


months=["jan","feb","march"]
number=[1,2,3,4,5,6,7,8,9]
num_dic={x:x*3 for x in number }
print("Using one input list to create dict: ", num_dic)


month_dict={key:value for (key,value) in zip(number,months)}
print("using two lists",month_dict)