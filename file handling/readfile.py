import random
f_name=input('type the file name')
f=open(f_name,'r')
f_content=f.read()
f_content_list=f_content.split("\n")
print(random.choice(f_content_list))