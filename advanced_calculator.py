from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		self.op=Stack()
		self.num=Stack()
		self.history=super().history
		pass
	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		if self.check_brackets(input_expression)==False:
			self.history.insert(0,(input_expression,"Error"))
			return "Error"
		
			

		ie = list("("+input_expression+")")
		
		a=""
		o=["(",")","{","}","+","-","/","*"]
		ope=["(","{"]
		clo=[")","}"]
		pr ={"{":0,"(":0,"+":1,"-":1,"*":2,"/":3}
		try:
			for i in range(len(ie)):
				
				if ie[i]==" " or ie[i] in o:
					if a!="":
						self.num.push(int(a))
						a=""
				elif ie[i] in ["1","2","3","4","5","6","7","8","9","0"]:
					
					a=a+ie[i]
				else:
					self.history.insert(0,(input_expression,"Error"))
					return "Error"
				
				if ie[i] in o:
					if ie[i] in ope:
						
						self.op.push(ie[i])
					elif ie[i] in clo:
						
						while self.op.peek() not in ope:
							a1=self.num.pop()
							a2=self.num.pop()
							b=super().evaluate_expression(str(a2)+self.op.pop()+str(a1))
							
							self.num.push(b)
						self.op.pop()
					elif pr[ie[i]]>pr[self.op.peek()]:
						
						self.op.push(ie[i])
					else:
						
						while pr[ie[i]]<=pr[self.op.peek()]:
							
							a1=self.num.pop()
							a2=self.num.pop()
							b=super().evaluate_expression(str(a2)+self.op.pop()+str(a1))
							
							self.num.push(b)
						self.op.push(ie[i])
		
		except:
			self.history.insert(0,(input_expression,"Error"))
			return "Error"		
		result = self.num.pop()
		if self.history[0] != (input_expression,result):
			self.history.insert(0,(input_expression,result))
		return result
		pass

	def tokenize(self, input_expression):
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		l=[]
		a=""
		o=["-","+","/","*","(",")","{","}"]
		for i in input_expression:
			if i==" " or i in o:
				if a!="":
					l.append(int(a))
					a=""
					if i in o:
						l.append(i)
				elif i in o:
					l.append(i)

			elif i in ["1","2","3","4","5","6","7","8","9"]:
				a=a+i
		if a!=" " and a!="":
			l.append(int(a))
		return l
		pass		

	def check_brackets(self, list_tokens):
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		r=0
		y =0
		for i in list_tokens:
			if r>=0 and y>=0:
				if i == "(":
					r+=1
				elif i==")":
					r-=1
				elif i=="}":
					y-=1
				elif i=="{":
					y+=1
			else:
				return False
		if r==0 and y==0:
			return True
		else:
			return False
		pass

	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		st= ""
		for i in list_tokens:
			st=st+str(i)
		return self.evaluate_expression(st)
		pass

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.history
		pass
