file =open('text.txt',mode='r')
data =file.readline()
print (data)
file.close()

#######################################################################################
#another way
#with open('text.txt','r') as file:
  #data=file.readline()
  #print(data)