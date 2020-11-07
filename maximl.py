'''
Name: Bhavesh Patel
Id: 201752013
'''


def count_distinct(s):
    return len(set(s))

def maximl(s):
    dist = count_distinct(s)
    minm = dist
    maxm = len(s)
    for i in range(len(s)):
        if dist == count_distinct(s[i:]):
            temp = s[i:]
        else:
            break
    ss = temp[::-1]
    for i in range(len(ss)):
        if dist == count_distinct(ss[i:]):
            temp2 = ss[i:]
        else:
            break
    # print(temp2)
    return len(temp2)
if __name__ == '__main__':
    s = input("input string of lowercase : ")
    print(maximl(s))