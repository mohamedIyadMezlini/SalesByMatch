n=int(input())
lst = list(map(int,input().split()))
pairs = sum([lst.count(i)//2 for i in set(lst)])
print(pairs)