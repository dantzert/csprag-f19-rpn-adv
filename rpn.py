#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'^': operator.pow,
	'/': operator.floordiv,
}

def calculate(string):
	stack = list()
	for token in string.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError: # this must be an operator
			try: 
				
				function = operator.__dict__[token]

			except KeyError:
				function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1,arg2)
			stack.append(result)
		
	if len(stack) != 1:
		raise TypeError("malformed input: "+ string)
	print(stack[0])
	return stack.pop()

def main():
	while True:
		calculate(input('rpn calc> '))

if __name__ == '__main__':
	main()
