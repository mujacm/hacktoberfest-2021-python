def binarySearch (a, l, r, x):

	if r >= l:

		mid = l + (r - l) // 2

		if a[mid] == x:
			return mid
		
		elif a[mid] > x:
			return binarySearch(a, l, mid-1, x)

		else:
			return binarySearch(a, mid + 1, r, x)

	else:
		return -1


arr = [ 21, 53, 64, 10, 40 ,12, 13, 94]
x = 12

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
