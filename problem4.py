# this one uses a for loop
x=[]
n=int(input("Enter number of elements:"))

for i in range(0,n):
	ele=int(input())
	x.append(ele)

y = []
 
for i in x:
    if i not in y:
      y.append(i)
  
print(y)

