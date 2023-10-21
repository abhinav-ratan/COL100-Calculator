from stack import Stack

class SimpleCalculator:
	history = []
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.history=[]
		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		for i in self.history:
			if input_expression==i[0]:
				return i[1]
		o=["+","-","/","*"]
		le = input_expression.strip()
		try:
			for i in range(1,len(le)):
				if le[i]=="+":
					self.history.insert(0,(input_expression,float(le[:i])+float(le[i+1:])))
					return float(le[:i])+float(le[i+1:])
				elif le[i]=="-":
					self.history.insert(0,(input_expression,float(le[:i])-float(le[i+1:])))
					return float(le[:i])-float(le[i+1:])
				elif le[i]=="/":
					self.history.insert(0,(input_expression,float(le[:i])/float(le[i+1:])))	
					return float(le[:i])/float(le[i+1:])
				elif le[i]=="*":
					self.history.insert(0,(input_expression,float(le[:i])*float(le[i+1:])))
					return float(le[:i])*float(le[i+1:])
			else:
				self.history.insert(0,(input_expression,"Error"))
				return "Error"

				
		except:
			self.history.insert(input_expression,"Error")
			return "Error"

		pass 

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.history
		pass
