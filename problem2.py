lst=[]
n=int(input("Enter number of elements:"))

for i in range(0,n):
	ele=int(input())
	lst.append(ele)


new_list=[]

for item in lst:
	if item < 5:
		new_list.append(item)

print(new_list)