class lazy(object):
	def __init__(self, func, num):
		# print 'lazy init with num' + str(num)
		self.func = func
		self.num = num
		self.total = 0
		self.args = num
	def __call__(self, *args):
		if(len(args) == 0):
			self.func(0, self.args)
			self.args = 0
			return self.num
		else:
			self.total = 0
			self.args = self.num
			for each in args:
				self.total += each
				self.args += each

			return lazy(self.func, self.args)

class eager(object):
	def __init__(self, func, num):
		self.func = func
		self.num = num
		self.total = 0
		self.args = 0
	def __call__(self, *args):
		if(len(args) == 0):
			return self.num
		else:
			# self.total = self.num
			self.total = 0
			self.args = self.num
			for each in args:
				self.total += each
				self.args += each

			self.func(0, self.total)

			return eager(self.func, self.args)

def curry(func, num, str='Eager'):
	if(str is 'Eager'):
		return eager(func, num)
	elif(str is 'Lazy'):
		return lazy(func, num)

add2 = lambda x, y : x + y  
adder = curry(add2, 5) # creates a 5 adder
print adder()
adder = adder(3) # creates an 8 adder 
print adder() # prints 8
print adder(2)() # prints 10
print adder(1)() # prints 9
adder = adder(3) # creates an 11 adder
print adder() # prints 11
print

adder0 = curry(add2, 0) # Eager
adder18 = adder0(3)(4,5)(6)
print adder18() # prints 18
print adder18(2)() # prints 20
print

lazyAdder0 = curry(add2, 0, 'Lazy')
lazyAdder18 = lazyAdder0(3)(4,5)(6)
print lazyAdder18() # prints 18
print lazyAdder18(2)() # prints 20

def sleepingAdd(x, y):
        import time
        for i in xrange(0, y):
            print ".",
            time.sleep(1);
        return x + y;
    
sadder0 = curry(sleepingAdd, 0)
print "Hey",
sadder10 = sadder0(3)(4,2)(1) # sleeps 10 secs (prints 10 dots) 
print "Yo"
print sadder10() # prints 10
print "Hey",
sadder10() # returns 10
print "Yo"
print

lazySadder0 = curry(sleepingAdd, 0, 'Lazy')
print "Hey",
lazySadder10 =  lazySadder0(3)(4,2)(1) 
print "Yo"
print lazySadder10() # sleeps 10 secs (prints 10 dots), prints 10
print "Hey",
lazySadder10() # returns 10
print "Yo"
