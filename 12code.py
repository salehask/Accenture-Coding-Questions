def Rearrange(str1,str2):
    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()
    return l1==l2

str1=input()
str2=input()
print(Rearrange(str1,str2))