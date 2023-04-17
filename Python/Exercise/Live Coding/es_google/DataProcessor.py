#Data Processing 
import pandas as pd 
import numpy as np 

class cleaning:
	def __init__(self)
		pass

	def remove_symbol(self,df,col,symbol)
		df.col.replace(symbol, '')
		return df

	def remove_and_convert(self,df,col,symbol)
		df.col.apply(lambda x: self.remove_symbol(df,col,symbol)).apply(lambda x: float(x))	
		return df