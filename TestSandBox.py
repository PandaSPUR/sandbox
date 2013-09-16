print '-' * 40
print "Test program that counts from 10 to 1 and print it"
for i in range(10):
	print 10 - i
print '-' * 40

def fib(n):
	result = []
	a, b = 0, 1
	for i in range(10):
		result.append(a)
		a, b = b, a + b
	return result

print "Test Fiboncci program"
print fib(10)


		
