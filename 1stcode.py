def diff(str1,len):
    if str1 is None:
        return 0
    else:
       temp=str1.split()
       hard=0
       easy=0
       for i in temp:
           con=0
           vow=0
           c=0
           flag=0
           
           for j in i:
               if j in "aeiou":
                   vow+=1
                   c=0
               else:
                   con+=1
                   c+=1
                   if c ==3:
                       flag=1
           if con>vow or flag:
               hard+=1
           else:
               easy+=1
       print(hard,easy)
    return (5*hard)-(2*easy)

str=input()
len=int(input())
result=diff(str,len)
print(result)


    