
def sumArray(r):
    sum=0
    ls = []

    for j in range(r):
        n = int(input())
        ls.append(n)

    for i in ls:
        sum+=i
   
    return sum

r = int(input())
print(sumArray(r))