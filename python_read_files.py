with open('sample.txt','r') as file:
    print(file.read(5))  #run only first 5 char.



with open('sample.txt','r') as file:
    print(file.readline()) 


with open('sample.txt','r') as file:
    print(file.readlines()) # return alist of lines


with open('sample.txt','r') as file:
   data= file.readlines() 
   for x in data:
     print(x)