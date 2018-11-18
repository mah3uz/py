arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 60
y = 9

def search(array, x):
	for i in range(len(array)):
		if array[i] == x:
			return i

		return -1

print(search(arr, x))
print(search(arr, y))
