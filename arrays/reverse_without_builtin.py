arr=[1,2,4,8,9]
n=len(arr)
for i in range(n//2):
	temp=arr[i]
	arr[i]=arr[n-1-i]
	arr[n-1-i]=temp
	
print(arr)
