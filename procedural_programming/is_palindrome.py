def isPlaindrome(str):
    start_ind=0
    end_ind=len(str)-1
    for x in str:
        if str[start_ind] != str[end_ind]:
            return False
    return True


print(isPlaindrome("racecar"))            