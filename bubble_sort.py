num=[5,7,4,8,9,2]
def bubblesort(num):
    for i in range(len(num)-1,0,-1):
    for j in range(i):
    if num[j]>num[j+1]:
    num[j],num[j+1]=num[j+1],num[j]
bubblesort(num)
print(num)
