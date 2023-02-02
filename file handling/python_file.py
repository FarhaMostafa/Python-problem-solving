try:
    with open('newfile3.txt','r')as file:
        file.writelines(["/n hi","/n hallo","/n shcuce"])
except FileNotFoundError as e:
    print("error",e)        