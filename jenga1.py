#Numbers divisble by 7 and 3
def result(N):
	for num in range(N):
			if num % 7 == 0 and num % 3== 0:
				print(str(num) + " ", end = "")
				
			else:
				pass
if __name__ == "__main__":
	N = 100
	result(N)

#divisible by 7 but not 3
def countNumbers(X, Y, N):

	count = 0;
	for i in range(1, N + 1):
		if ((i % 7 == 0) and (i % 3 != 0)):
			count += 1;

	return count;
X = 7;
Y = 3;
N = 100;
print(countNumbers(X, Y, N));
	
# This code is contributed by mits
