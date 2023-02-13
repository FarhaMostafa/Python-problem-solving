data=[1,2,3,4,5,6,7,8,9,10]
gen_obj=(x for x in data)
print(gen_obj)
print(type(gen_obj))

for items in gen_obj:
    print(items,end=" ")


a = [[96], [69]]

print("".join(list(map(str, a))))



z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)


