def string_revrse(str):
    if len(str)==0:
        return str
    else:
        return string_revrse(str[1:])+str[0]

str="reversal"
reverse=string_revrse(str)    
print(reverse)