
# s="aaabbb"
# if len(s)%2==0:
#     mid=len(s)/2
#     s1=sorted(s[0:int(mid)])
#     s2=sorted(s[int(mid):])
#     c=0
#     for i,j in zip(s1,s2):
#         if i != j:
#             c=c+1
# print(c)
from collections import Counter
# s="fdhlvosfpafhalll"
#
# mid=len(s)/2
# s1=s[0:int(mid)]
# s2=s[int(mid):]
#
# c1 = Counter(s1)
# print(c1)
# c2 = Counter(s2)
# print(c2)
# d3=c1-c2
# print(d3)
# print(sum(d3.values()))

s="oagciicgaoyjmahhamjymmwjnnjwmmvpxhpphxpvlikappakilyygvkkvgyymlpfddfplmhiodvvdoihfxpkggkpxfuevvuuvveu"
# s="aabac"
# i=0
# while i < len(s)-1:
#     if s[i] == s[i + 1]:
#         # s = s.replace(s[i], "",2)
#         s = s[:i] + s[i + 2:]
#         i=0
#     else:
#         i+=1
# print(s)

# def runningTime(arr):
#     # Write your code here
#     c = 0
#     for j in range(1,len(arr)):
#         key=arr[j]
#         i=j-1
#         while i>=0 and key>arr[i]:
#             arr[i+1]=arr[i]
#             i-=1
#         arr[i+1]=key
#
#     return arr
#
# print(runningTime([4 ,4 ,3 ,4,2,43,6,2,4,1,34,2]))
# a=[4 ,4 ,3 ,4]
# print(a.index(3))


# def is_prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(is_prime(-1))

# num=1234
# rev=0
# while num>0:
#     temp=num%10
#     rev=rev*10+temp
#     num=num//10
# print(rev)

import random
s=""
for _ in range (10):
    c=chr(random.randint(65, 90))
    s=s+c

# def palindrome(s):
#     if len(s)<=1:
#         return None
#     if s[0]!=s[-1]:
#         return "not a palindrome"
#     return palindrome(s[1:len(s)])
#
#
# if palindrome("acca")==None:
#     print(" palindrome")
# else:print(" n palindrome")

# def palindrome(s):
#     if len(s) <= 1:
#         return "palindrome"
#     else:
#         if s[0]==s[-1]:
#             return palindrome(s[1:-1])
#         else:return "not a palindrome"
#
# print(palindrome("aba"))

# s="abaca"
# p1=0
# p2=-1
# for i in range(len(s)//2):
#     if s[p1]==s[p2]:
#         p1+=1
#         p2-=1
#     else:
#         print("not a palindrome")
#         exit()
# else:print("palindrome")

n="4757362"
k=10000
# k=reversed
print(reversed(str(k)))
# n=n*k
# n=int(n)
#
# while k>0:
#     s=0
#     # print(n)
#     while n>0:
#         temp=n%10
#         s+=temp
#         n=n//10
#     n=s
#     k-=1
# print(s)
# k=1600
# while k%10==0:
#         k=k/10
# print(k)

# def fib(n):
#
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(10))
# n=10
# sum=0
# n1=0
# n2=1
# for i in range (n-1):
#
#     sum=n1+n2
#     n1=n2
#     n2=sum
# print(sum)
