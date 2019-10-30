#!/usr/bin/env python3

import operator
import math # support singleton operations

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

			if (len(stack) == 2):

				try: 
				
					function = operator.__dict__[token]
				except KeyError:
			
					function = operators[token]
			
			
			
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1,arg2)
				stack.append(result)
			elif (len(stack) == 1):
				try:
					function = math.__dict__[token]

				except KeyError:

					raise TypeError("no singleton function found for: "+ string)

				arg = stack.pop()
				result = function(arg)
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
