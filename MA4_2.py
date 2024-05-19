#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n<=1:
		return n
	else:
		return (fib_py(n-1)+fib_py(n-2))
		
@njit
def fib_numba(n):
	if n<=1:
		return n
	else:
		return (fib_numba(n-1)+fib_numba(n-2))


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())
	
	start_py = pc()
	py = fib_py(10)
	end_py = pc()
	print("Python fib(10) = ", py, "	Time = ", end_py-start_py)
	
	start_num = pc()
	num = fib_numba(47)
	end_num = pc()
	print("Numba fib(47) = ", num, "	Time = ", end_num-start_num)
	
	start_pers = pc()
	C_fib = Person(47)
	pers = C_fib.fib()
	end_pers = pc()
	print("C++ Person fib(47) = ", pers, "	Time = ", end_pers-start_pers)
	
	
	
	t_py = []
	t_num = []
	t_pers = []
	n = []
	for i in range(0,1):
		n.append(i)
		start_py = pc()
		py = fib_py(i)
		end_py = pc()
		t_py.append(end_py-start_py)
		
		start_num = pc()
		num = fib_numba(i)
		end_num = pc()
		t_num.append(end_num-start_num)
		
		start_pers = pc()
		test = Person(i)
		test.fib()
		end_pers = pc()
		t_pers.append(end_pers-start_pers)
	
	ax = plt.subplot()
	ax.plot(n, t_py, 'b.')
	ax.plot(n, t_num, 'r.')
	ax.plot(n, t_pers, 'g.')
	#plt.show()
	
	#plt.savefig('py_numba_pers.png', bbox_inches='tight')

if __name__ == '__main__':
	main()





