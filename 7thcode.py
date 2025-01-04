#fREQUENTCHARACTERREPLACED


def FrequenctCharacterReplaced(arr,n):
    if arr ==None:
        return -1
    else:
        maximum=-9999999
        for i in range(arr):
            c=arr.count(i)
            if c > maximum:
                maximum=c
                char=i
            elif c == maximum:
                if i < char:
                    char=i
    return arr.replace(char,n)


arr=input().split(' ')
n = input()
result=FrequenctCharacterReplaced(arr,n)
print(result)











arr=input()
n = input()