
# -*- coding: utf8 -*-
import time 
def comput():
	n =int(input('请输入要计算圆周率的长度：'))
	start_time = time.time()
	w = n+10
	b = 10**w
	x1 = b*4//5
	x2 = b// -239
	he = x1+x2
	n *= 2
	for i in range(3,n,2):
	    x1 //= -25
	    x2 //= -57121
	    x = (x1+x2) // i
	    he += x
	pai = he*4
	pai //= 10**10
	end_time = time.time()
	run_time = str(end_time - start_time)
	print ('运行时间：' + run_time )
	print ('计算结果:',pai)
	print ('\n'*3) 
	comput()
comput()
